import asyncio
from typing import Callable, Coroutine, Any, TYPE_CHECKING
from abc import ABC, abstractmethod

from ..exceptions import EventFunctionTaskError
from .responses import EventResponse


if TYPE_CHECKING:
    from .._client import MercadoLivreAffiliates


class Event(ABC):
    def __init__(self) -> None:
        self.__event_functions: set[Callable[[MercadoLivreAffiliates, EventResponse], Coroutine[Any, Any, None]]] = set()
        self.__started = False
        self.__event_functions_tasks: set[asyncio.Task[None]] = set()
        self.__start_task: asyncio.Task[None] | None = None

    @property
    def total_event_functions(self) -> int:
        return len(self.__event_functions)

    @property
    def started(self) -> bool:
        return self.__started
    
    async def start(self, client: MercadoLivreAffiliates) -> None:
        self.__started = True
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

    def register_event_function(self, function: Callable[[MercadoLivreAffiliates, EventResponse], Coroutine[Any, Any, None]]) -> None:
        self.__event_functions.add(function)
    
    def remove_event_function(self, function: Callable[[MercadoLivreAffiliates, EventResponse], Coroutine[Any, Any, None]]) -> None:
        self.__event_functions.discard(function)

    @abstractmethod
    async def _event_logic(self) -> EventResponse:
        pass

    async def __start(self, client: MercadoLivreAffiliates) -> None:
        while self.started:
            event_respone = await self._event_logic()
            for event_function in self.__event_functions:
                event_function_task = asyncio.create_task(coro=event_function(client, event_respone))
                self.__event_functions_tasks.add(event_function_task)
                event_function_task.add_done_callback(self.__finish_event_function_task)

    def __finish_event_function_task(self, event_function_task: asyncio.Task[None]) -> None:
        self.__event_functions_tasks.discard(event_function_task)
        try:
            event_function_task.result()
        except asyncio.CancelledError:
            pass
        except Exception as error:
            raise EventFunctionTaskError(f"Failed on executing event function: {error}")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


class DayOffers(Event):
    def __init__(self) -> None:
        super().__init__()
    
    async def _event_logic(self) -> EventResponse:
        await asyncio.sleep(0)
        print("DayOffers")
        return EventResponse()
    

class LightningOffers(Event):
    def __init__(self) -> None:
        super().__init__()
    
    async def _event_logic(self) -> EventResponse:
        await asyncio.sleep(0)
        print("LightningOffers")
        return EventResponse()
    