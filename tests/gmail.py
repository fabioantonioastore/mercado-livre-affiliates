import asyncio
import os

import dotenv

from mercado_livre_affiliates._impl.services import Gmail
from mercado_livre_affiliates._impl.utils.mercado_livre_affiliates import (
    extract_mercado_livre_verification_code_from_mail,
)

dotenv.load_dotenv()
APP_PASSWORD = str(os.getenv("APP_PASSWORD"))


async def main() -> None:
    async with Gmail(
        gmail_address="astore.a.fabio@gmail.com", app_password=APP_PASSWORD
    ) as gmail:
        mail_content = await gmail.fetch_last_sender_mail_content(
            sender="Mercado Livre"
        )
        if mail_content:
            print(
                extract_mercado_livre_verification_code_from_mail(
                    mail_content=mail_content
                )
            )
        else:
            print(mail_content)


asyncio.run(main=main())
