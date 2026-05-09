from types import TracebackType

from aioimaplib import IMAP4_SSL  # type: ignore


class GmailClient:
    def __init__(self, gmail: str, app_password: str) -> None:
        self.__gmail = gmail
        self.__app_password = app_password
        self.__client: IMAP4_SSL | None = None

    @property
    def gmail(self) -> str:
        return self.__gmail

    async def __is_alive(self) -> bool:
        if self.__client is None:
            return False
        try:
            await self.__client.noop()
            return True
        except Exception:
            return False

    async def __connect(self) -> IMAP4_SSL:
        client = IMAP4_SSL(host="imap.gmail.com", port=993)
        await client.wait_hello_from_server()
        await client.login(user=self.__gmail, password=self.__app_password)
        return client

    async def get_client(self) -> IMAP4_SSL:
        if self.__client and await self.__is_alive():
            return self.__client
        await self.close()
        self.__client = await self.__connect()
        return self.__client

    async def close(self) -> None:
        if self.__client is not None:
            try:
                await self.__client.logout()
            except Exception:
                pass
            finally:
                self.__client = None

    async def __aenter__(self) -> IMAP4_SSL:
        return await self.get_client()

    async def __aexit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None) -> None:
        await self.close()

    def __repr__(self) -> str:
        return "GmailClient()"
