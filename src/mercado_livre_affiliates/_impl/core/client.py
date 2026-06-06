import asyncio
from uuid import UUID
from contextlib import AbstractAsyncContextManager, asynccontextmanager
from types import TracebackType
from typing import AsyncGenerator, Any

from playwright.async_api import async_playwright, Playwright, Browser, BrowserContext

from .session import MercadoLivreAffiliatesSession
from ..exceptions import (
    StartError,
    BrowserNotStartedError,
    CreateSessionError,
    CloseSessionError,
    BackgroundSessionError,
)


class MercadoLivreAffiliates(AbstractAsyncContextManager["MercadoLivreAffiliates"]):
    def __init__(self) -> None:
        self.__sessions: dict[UUID, MercadoLivreAffiliatesSession] = {}
        self.__playwright: Playwright | None = None
        self.__browser: Browser | None = None
        self.__background_sessions_events: dict[UUID, asyncio.Event] = {}
        self.__background_sessions_tasks: dict[UUID, asyncio.Task[Any] | None] = {}
        self.__lock = asyncio.Lock()

    @property
    def sessions(self) -> list[MercadoLivreAffiliatesSession]:
        return list(self.__sessions.values())

    async def get_session(self, session_uuid: UUID) -> MercadoLivreAffiliatesSession:
        return self.__sessions[session_uuid]

    async def end_session(self, session_uuid: UUID) -> None:
        try:
            async with self.__lock:
                if session_uuid in self.__background_sessions_events:
                    session_event = self.__background_sessions_events.pop(session_uuid)
                    session_event.set()
                if session_uuid in self.__background_sessions_tasks:
                    session_task = self.__background_sessions_tasks.pop(session_uuid)
                    if session_task is not None and not session_task.done():
                        session_task.cancel()
                if session_uuid in self.__sessions:
                    session = self.__sessions.pop(session_uuid)
                    await session.close()
        except Exception as error:
            raise CloseSessionError(f"Unable to close session: {error}")

    @asynccontextmanager
    async def create_session(
        self, gmail_address: str, app_password: str
    ) -> AsyncGenerator[MercadoLivreAffiliatesSession, Any]:
        browser_context = await self.__create_browser_context()
        session_uuid = None
        try:
            async with MercadoLivreAffiliatesSession(
                gmail_address=gmail_address,
                app_password=app_password,
                browser_context=browser_context,
            ) as session:
                self.__sessions[session.uuid] = session
                session_uuid = session.uuid
                yield session
        except asyncio.CancelledError:
            raise
        except Exception as error:
            raise CreateSessionError(f"Error on create session: {error}")
        finally:
            if not browser_context.is_closed():
                await browser_context.close()
            if session_uuid is not None:
                await self.end_session(session_uuid=session_uuid)

    async def create_background_session(
        self, gmail_address: str, app_password: str
    ) -> None:
        asyncio.create_task(
            coro=self.__background_session(
                gmail_address=gmail_address, app_password=app_password
            )
        )

    async def __background_session(self, gmail_address: str, app_password: str) -> None:
        try:
            async with self.create_session(
                gmail_address=gmail_address, app_password=app_password
            ) as session:
                self.__background_sessions_events[session.uuid] = asyncio.Event()
                self.__background_sessions_tasks[session.uuid] = asyncio.current_task()
                await self.__background_sessions_events[session.uuid].wait()
        except asyncio.CancelledError:
            raise
        except Exception as error:
            raise BackgroundSessionError(
                f"A error occurs during background session: {error}"
            )

    async def __create_browser_context(self) -> BrowserContext:
        browser = self.__get_browser()
        return await browser.new_context(
            user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/637.36 Chrome/120 Safari/537.36",
            locale="pt-BR",
            timezone_id="America/Sao_Paulo",
            viewport={"width": 1280, "height": 720},
        )

    def __get_browser(self) -> Browser:
        if self.__browser is None:
            raise BrowserNotStartedError("Browser is not started yet")
        return self.__browser

    async def __start(self) -> None:
        try:
            self.__playwright = await async_playwright().start()
            self.__browser = await self.__playwright.chromium.launch(
                headless=True, args=["--disable-blink-features=AutomationControlled"]
            )
        except Exception as error:
            raise StartError(
                f'A error occurs on trying start client: {error}, try run "playwright install chromium"'
            )

    async def __stop(self) -> None:
        for session in self.sessions:
            await self.end_session(session_uuid=session.uuid)
        await asyncio.sleep(1)
        if self.__browser is not None:
            await self.__browser.close()
            self.__browser = None
        if self.__playwright is not None:
            await self.__playwright.stop()
            self.__playwright = None

    async def __aenter__(self) -> "MercadoLivreAffiliates":
        await self.__start()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        await self.__stop()
