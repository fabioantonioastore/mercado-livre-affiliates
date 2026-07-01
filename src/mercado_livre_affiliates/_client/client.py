import asyncio
from contextlib import AbstractAsyncContextManager, asynccontextmanager
from types import TracebackType
from typing import Self, Callable, Coroutine, Any, AsyncIterator, overload

from playwright.async_api import (
    Playwright,
    BrowserContext,
    Browser,
    async_playwright,
)

from ..events import DealsOfTheDay, LightningDeals
from .._models import EventResponse, DealOfTheDayProduct, LightningDealProduct
from ..exceptions import SessionAlreadyExistError
from .session import MercadoLivreAffiliatesSession


class MercadoLivreAffiliates(AbstractAsyncContextManager["MercadoLivreAffiliates"]):
    def __init__(self, browser: Browser | None = None) -> None:
        self.__playwright: Playwright | None = None
        self.__browser: Browser | None = browser
        self.__browser_context: BrowserContext | None = None
        self.__event_browser_context: BrowserContext | None = None
        self.__day_offers_event = DealsOfTheDay()
        self.__lightning_offers_event = LightningDeals()
        self.__sessions: dict[str, MercadoLivreAffiliatesSession] = {}

    async def __aenter__(self) -> Self:
        await self.__start()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.__stop()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    @asynccontextmanager
    async def create_session(
        self, gmail_address: str, app_password: str
    ) -> AsyncIterator[MercadoLivreAffiliatesSession]:
        if gmail_address in self.sessions:
            raise SessionAlreadyExistError(
                f"Session with gmail address {gmail_address} already exist"
            )
        async with MercadoLivreAffiliatesSession(
            gmail_address=gmail_address,
            app_password=app_password,
            browser_context=await self.__create_browser_context(),
        ) as session:
            try:
                self.sessions[gmail_address] = session
                yield session
            finally:
                self.sessions.pop(gmail_address, None)

    @property
    def sessions(self) -> dict[str, MercadoLivreAffiliatesSession]:
        return self.__sessions

    @overload
    def register_event_function_decorator(self, event: type[DealsOfTheDay]) -> Callable[
        [
            Callable[
                ["MercadoLivreAffiliates", DealOfTheDayProduct],
                Coroutine[Any, Any, None],
            ]
        ],
        Callable[
            ["MercadoLivreAffiliates", DealOfTheDayProduct], Coroutine[Any, Any, None]
        ],
    ]:
        pass

    @overload
    def register_event_function_decorator(
        self, event: type[LightningDeals]
    ) -> Callable[
        [
            Callable[
                ["MercadoLivreAffiliates", LightningDealProduct],
                Coroutine[Any, Any, None],
            ]
        ],
        Callable[
            ["MercadoLivreAffiliates", LightningDealProduct], Coroutine[Any, Any, None]
        ],
    ]:
        pass

    def register_event_function_decorator(
        self, event: type[DealsOfTheDay] | type[LightningDeals]
    ) -> Callable[[Any], Any]:
        def decorator(
            function: (
                Callable[
                    ["MercadoLivreAffiliates", DealOfTheDayProduct],
                    Coroutine[Any, Any, None],
                ]
                | Callable[
                    ["MercadoLivreAffiliates", LightningDealProduct],
                    Coroutine[Any, Any, None],
                ]
            ),
        ) -> (
            Callable[
                ["MercadoLivreAffiliates", DealOfTheDayProduct],
                Coroutine[Any, Any, None],
            ]
            | Callable[
                ["MercadoLivreAffiliates", LightningDealProduct],
                Coroutine[Any, Any, None],
            ]
        ):
            if issubclass(event, DealsOfTheDay):
                self.__day_offers_event.register_event_function(function=function)  # type: ignore[arg-type]
                if not self.__day_offers_event.started:
                    asyncio.create_task(self.__day_offers_event.start(client=self))
            else:
                self.__lightning_offers_event.register_event_function(function=function)  # type: ignore[arg-type]
                if not self.__lightning_offers_event.started:
                    asyncio.create_task(
                        self.__lightning_offers_event.start(client=self)
                    )
            return function

        return decorator

    @overload
    async def register_event_function(
        self,
        event: type[DealsOfTheDay],
        function: Callable[
            ["MercadoLivreAffiliates", DealOfTheDayProduct], Coroutine[Any, Any, None]
        ],
    ) -> None: ...

    @overload
    async def register_event_function(
        self,
        event: type[LightningDeals],
        function: Callable[
            ["MercadoLivreAffiliates", LightningDealProduct], Coroutine[Any, Any, None]
        ],
    ) -> None: ...

    async def register_event_function(
        self,
        event: type[DealsOfTheDay] | type[LightningDeals],
        function: (
            Callable[
                ["MercadoLivreAffiliates", DealOfTheDayProduct],
                Coroutine[Any, Any, None],
            ]
            | Callable[
                ["MercadoLivreAffiliates", LightningDealProduct],
                Coroutine[Any, Any, None],
            ]
        ),
    ) -> None:
        if issubclass(event, DealsOfTheDay):
            self.__day_offers_event.register_event_function(function=function)  # type: ignore[arg-type]
            if not self.__day_offers_event.started:
                await self.__day_offers_event.start(client=self)
            return
        self.__lightning_offers_event.register_event_function(function=function)  # type: ignore[arg-type]
        if not self.__lightning_offers_event.started:
            await self.__lightning_offers_event.start(client=self)

    async def remove_event_function(
        self,
        function: Callable[
            ["MercadoLivreAffiliates", EventResponse], Coroutine[Any, Any, None]
        ],
    ) -> None:
        self.__day_offers_event.remove_event_function(function=function)
        if self.__day_offers_event.total_event_functions == 0:
            await self.__day_offers_event.stop()
        self.__lightning_offers_event.remove_event_function(function=function)
        if self.__lightning_offers_event.total_event_functions == 0:
            await self.__lightning_offers_event.stop()

    async def _get_event_browser_context(self) -> BrowserContext:
        if self.__event_browser_context is None:
            self.__event_browser_context = await self.__create_event_browser_context()
        return self.__event_browser_context

    async def __create_event_browser_context(self) -> BrowserContext:
        if self.__event_browser_context is None:
            self.__event_browser_context = await self.__create_browser_context()
        return self.__event_browser_context

    async def __create_browser(self) -> Browser:
        playwright = await self.__get_playwright()
        return await playwright.chromium.launch(
            headless=True, args=["--disable-blink-features=AutomationControlled"]
        )

    async def __create_browser_context(self) -> BrowserContext:
        if self.__browser is None:
            self.__browser = await self.__create_browser()
        return await self.__browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/637.36 Chrome/120 Safari/537.36",
            locale="pt-BR",
            timezone_id="America/Sao_Paulo",
        )

    async def __start(self) -> None:
        self.__playwright = await async_playwright().start()

    async def __stop(self) -> None:
        for session in self.sessions.values():
            await session.close()
        self.sessions.clear()
        if self.__day_offers_event.started:
            await self.__day_offers_event.stop()
        if self.__lightning_offers_event.started:
            await self.__lightning_offers_event.stop()
        if (
            self.__event_browser_context is not None
            and not self.__event_browser_context.is_closed()
        ):
            await self.__event_browser_context.close()
        if (
            self.__browser_context is not None
            and not self.__browser_context.is_closed()
        ):
            await self.__browser_context.close()
        if self.__playwright is not None:
            await self.__playwright.stop()
        self.__event_browser_context = None
        self.__browser_context = None
        self.__playwright = None

    async def __get_playwright(self) -> Playwright:
        if self.__playwright is None:
            raise ValueError("Application not started yet")
        return self.__playwright
