import asyncio
from datetime import datetime, timezone, timedelta
from typing import Callable, Coroutine, Any, AsyncGenerator, Generic, TYPE_CHECKING
from abc import ABC, abstractmethod

from playwright.async_api import BrowserContext

from .exceptions import EventFunctionTaskError, EventNotStartedError, EventLogicError
from ._models import LightningDealProduct, DealOfTheDayProduct, EventResponseT
from ._utils.events import (
    web_scraping_deals_of_the_day_products,
    web_scraping_lightning_deals_products,
)

if TYPE_CHECKING:
    from ._client import MercadoLivreAffiliates


LightningDealMaxDurationSeconds = 6 * 60 * 60
DayDealMaxDurationDays = 1


class Event(ABC, Generic[EventResponseT]):
    def __init__(self) -> None:
        self.__event_functions: set[
            Callable[
                [MercadoLivreAffiliates, EventResponseT], Coroutine[Any, Any, None]
            ]
        ] = set()
        self.__started = False
        self.__event_functions_tasks: set[asyncio.Task[None]] = set()
        self.__start_task: asyncio.Task[None] | None = None
        self.__browser_context: BrowserContext | None = None
        self._event = asyncio.Event()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    @property
    def total_event_functions(self) -> int:
        return len(self.__event_functions)

    @property
    def started(self) -> bool:
        return self.__started

    async def start(self, client: MercadoLivreAffiliates) -> None:
        self.__started = True
        self.__browser_context = await client._get_event_browser_context()  # type: ignore
        self._event.set()
        self.__start_task = asyncio.create_task(coro=self.__start(client=client))

    async def stop(self) -> None:
        self.__started = False
        if self.__start_task is not None and not self.__start_task.done():
            self.__start_task.cancel()
        for event_function_task in self.__event_functions_tasks:
            if not event_function_task.done():
                event_function_task.cancel()
        self.__event_functions_tasks.clear()
        self.__start_task = None
        self.__browser_context = None

    def register_event_function(
        self,
        function: Callable[
            [MercadoLivreAffiliates, EventResponseT], Coroutine[Any, Any, None]
        ],
    ) -> None:
        self.__event_functions.add(function)

    def remove_event_function(
        self,
        function: Callable[
            [MercadoLivreAffiliates, EventResponseT], Coroutine[Any, Any, None]
        ],
    ) -> None:
        self.__event_functions.discard(function)

    @abstractmethod
    async def _event_logic(self) -> AsyncGenerator[EventResponseT, None]:
        return
        yield

    def _get_browser_context(self) -> BrowserContext:
        if self.__browser_context is None:
            raise EventNotStartedError("Event don't started yet")
        return self.__browser_context

    async def __start(self, client: MercadoLivreAffiliates) -> None:
        while self.started:
            await self._event.wait()
            async for event_response in self._event_logic():
                for event_function in self.__event_functions:
                    event_function_task = asyncio.create_task(
                        coro=event_function(client, event_response)
                    )
                    self.__event_functions_tasks.add(event_function_task)
                    event_function_task.add_done_callback(
                        self.__finish_event_function_task
                    )
            if self._event.is_set():
                self._event.clear()

    def __finish_event_function_task(
        self, event_function_task: asyncio.Task[None]
    ) -> None:
        self.__event_functions_tasks.discard(event_function_task)
        try:
            event_function_task.result()
        except asyncio.CancelledError:
            pass
        except Exception as error:
            raise EventFunctionTaskError(f"Failed on executing event function: {error}")


class DealsOfTheDay(Event[DealOfTheDayProduct]):
    def __init__(self) -> None:
        super().__init__()

    async def _event_logic(self) -> AsyncGenerator[DealOfTheDayProduct, None]:
        browser_context = self._get_browser_context()
        page = await browser_context.new_page()
        try:
            async for product in web_scraping_deals_of_the_day_products(page=page):
                yield product
        except Exception as error:
            raise EventLogicError(f"A error occurs during event logic: {error}")
        finally:
            await page.close()
            delay = timedelta(days=DayDealMaxDurationDays).total_seconds()
            await asyncio.sleep(delay=delay)
            self._event.set()


class LightningDeals(Event[LightningDealProduct]):
    def __init__(self) -> None:
        super().__init__()

    async def _event_logic(self) -> AsyncGenerator[LightningDealProduct, None]:
        browser_context = self._get_browser_context()
        page = await browser_context.new_page()
        last_product_expires_in: datetime | None = None
        try:
            async for product in web_scraping_lightning_deals_products(page=page):
                last_product_expires_in = product.expires_in
                yield product
        except Exception as error:
            raise EventLogicError(f"A error occurs during event logic: {error}")
        finally:
            await page.close()
            if last_product_expires_in is None:
                target = datetime.now(tz=timezone.utc) + timedelta(
                    seconds=LightningDealMaxDurationSeconds
                )
                delay = (target - datetime.now(tz=timezone.utc)).total_seconds()
                await asyncio.sleep(delay=delay)
            else:
                delay = (
                    last_product_expires_in - datetime.now(tz=timezone.utc)
                ).total_seconds()
                await asyncio.sleep(delay=delay)
            self._event.set()
