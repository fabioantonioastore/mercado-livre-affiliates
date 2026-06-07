import asyncio

from mercado_livre_affiliates import MercadoLivreAffiliates
from mercado_livre_affiliates.events import DayOffers, LightningOffers, EventResponse


async def day_offers_test(client: MercadoLivreAffiliates, event_response: EventResponse) -> None:
    print("DayOffers test")


async def lightining_offers_test(client: MercadoLivreAffiliates, event_response: EventResponse) -> None:
    print("LightningOffers test")


async def main() -> None:
    async with MercadoLivreAffiliates(gmail_address="astore.a.fabio@gmail.com", app_password="test") as mercado_livre_affiliates:
        await mercado_livre_affiliates.register_event_function(event=DayOffers, function=day_offers_test)
        await mercado_livre_affiliates.register_event_function(event=LightningOffers, function=lightining_offers_test)
        print("Ok")
        await asyncio.sleep(10)


asyncio.run(main=main())
