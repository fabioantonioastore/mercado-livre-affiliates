import asyncio
import os

import dotenv
from mercado_livre_affiliates import MercadoLivreAffiliates

dotenv.load_dotenv()
APP_PASSWORD = str(os.getenv("APP_PASSWORD"))


async def main() -> None:
    async with MercadoLivreAffiliates() as mercado_livre_affiliates:
        await mercado_livre_affiliates.create_background_session(
            gmail_address="astore.a.fabio@gmail.com", app_password=APP_PASSWORD
        )
        await asyncio.sleep(1)
        print(mercado_livre_affiliates.sessions)
        for session in mercado_livre_affiliates.sessions:
            await mercado_livre_affiliates.end_session(session_uuid=session.uuid)
        print(mercado_livre_affiliates.sessions)


asyncio.run(main=main())
