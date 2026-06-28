from types import TracebackType
import email
from contextlib import AbstractAsyncContextManager

import aioimaplib  # type: ignore


class Gmail(AbstractAsyncContextManager["Gmail"]):
    def __init__(self, gmail_address: str, app_password: str) -> None:
        self.__gmail_address = gmail_address
        self.__app_password = app_password.replace(" ", "")
        self.__connection: aioimaplib.IMAP4_SSL | None = None

    async def __aenter__(self) -> "Gmail":
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        await self.__close()

    def __repr__(self):
        return f"{self.__class__.__name__}(gmail_address={self.gmail_address}, app_password=*)"

    @property
    def gmail_address(self) -> str:
        return self.__gmail_address

    async def fetch_last_sender_mail_content(self, sender: str) -> str | None:
        connection = await self.get_connection()
        await connection.select("INBOX")
        _, data = await connection.search(f'(FROM "{sender}")')  # type: ignore
        if not data or not data[0]:
            return None
        ids = data[0].split()  # type: ignore
        if not ids:
            return None
        last_id = ids[-1].decode()  # type: ignore
        _, message_data = await connection.fetch(last_id, "(RFC822)")  # type: ignore
        raw_email = None
        for part in message_data:  # type: ignore
            if isinstance(part, (bytes, bytearray)) and b"Delivered-To" in part:
                raw_email = bytes(part)
                break
        if raw_email is None:
            raise ValueError(f"Não encontrou email válido: {message_data}")
        message = email.message_from_bytes(raw_email)
        if message.is_multipart():
            for part in message.walk():
                payload = part.get_payload(decode=True)
                if payload is None:
                    continue
                content = payload.decode(errors="ignore")  # type: ignore
                return content  # type: ignore
        else:
            payload = message.get_payload(decode=True)
            if payload:
                content = payload.decode(errors="ignore")  # type: ignore
                return content  # type: ignore
        return None

    async def get_connection(self) -> aioimaplib.IMAP4_SSL:
        if await self.__connection_is_alive():  # type: ignore
            return self.__connection  # type: ignore
        self.__connection = await self.__create_connection()  # type: ignore
        return self.__connection  # type: ignore

    async def __create_connection(self) -> aioimaplib.IMAP4_SSL:
        connection = aioimaplib.IMAP4_SSL(host="imap.gmail.com", port=993)
        await connection.wait_hello_from_server()
        await connection.login(user=self.gmail_address, password=self.__app_password)
        return connection

    async def __connection_is_alive(self) -> bool:
        if self.__connection is None:
            return False
        try:
            await self.__connection.noop()
            return True
        except Exception:
            return False

    async def __close(self) -> None:
        if self.__connection is not None:
            try:
                await self.__connection.close()
                await self.__connection.logout()
            except Exception:
                pass
            finally:
                self.__connection = None
