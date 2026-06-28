import asyncio

from mercado_livre_affiliates import MercadoLivreAffiliates
from mercado_livre_affiliates.events import (
    DealsOfTheDay,
    LightningDeals,
    DealOfTheDayProduct,
    LightningDealProduct,
)


async def day_offers_test(
    client: MercadoLivreAffiliates, event_response: DealOfTheDayProduct
) -> None:
    print("DayOfferProduct")
    for key, value in dict(event_response).items():
        print(f"{key}: {value}")
    print("\n")


async def lightining_offers_test(
    client: MercadoLivreAffiliates, event_response: LightningDealProduct
) -> None:
    print("FlashOfferProduct")
    for key, value in dict(event_response).items():
        print(f"{key}: {value}")
    print("\n")


async def main() -> None:
    async with MercadoLivreAffiliates() as mercado_livre_affiliates:
        await mercado_livre_affiliates.register_event_function(
            event=LightningDeals, function=lightining_offers_test
        )
        await mercado_livre_affiliates.register_event_function(
            event=DealsOfTheDay, function=day_offers_test
        )
        await asyncio.sleep(100)


asyncio.run(main=main())
