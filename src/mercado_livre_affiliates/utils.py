import re
import email

from aioimaplib import IMAP4_SSL  # type: ignore


def extract_verification_code_from_email(text: str) -> str | None:
    match = re.search(r"\b\d{6}\b", text)
    if match:
        return match.group(0)
    return None


async def fetch_last_email_content(client: IMAP4_SSL) -> str | None:
    await client.select("INBOX")
    _, data = await client.search("ALL")  # type: ignore
    if not data or not data[0]:
        return None
    ids = data[0].split()  # type: ignore
    if not ids:
        return None
    last_id = ids[-1].decode()  # type: ignore
    _, message_data = await client.fetch(last_id, "(RFC822)")  # type: ignore
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
