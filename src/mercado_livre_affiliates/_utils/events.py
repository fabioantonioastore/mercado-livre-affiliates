from typing import AsyncGenerator, Any, Literal
from datetime import datetime, timedelta, timezone

from playwright.async_api import Page, Locator

from .._models import DealOfTheDayProduct, LightningDealProduct
from ..enums import OfferCategory

PRODUCTS_DEALS_BY_CATEGORIES: dict[str, set[str]] = {
    "https://www.mercadolivre.com.br/ofertas?category=MLB251478": {
        OfferCategory.antiques_and_collectibles.value(),
        OfferCategory.antiques_and_collectibles.antiques.value(),
        OfferCategory.antiques_and_collectibles.antiques.medal_holder.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB180312": {
        OfferCategory.antiques_and_collectibles.value(),
        OfferCategory.antiques_and_collectibles.antiques.value(),
        OfferCategory.antiques_and_collectibles.antiques.trophy.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB393901": {
        OfferCategory.antiques_and_collectibles.value(),
        OfferCategory.antiques_and_collectibles.flags.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1806": {
        OfferCategory.antiques_and_collectibles.value(),
        OfferCategory.antiques_and_collectibles.banknotes_and_coins.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2662": {
        OfferCategory.antiques_and_collectibles.value(),
        OfferCategory.antiques_and_collectibles.sculptures.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB433161": {
        OfferCategory.antiques_and_collectibles.value(),
        OfferCategory.antiques_and_collectibles.militaria_and_related_items.value(),
        OfferCategory.antiques_and_collectibles.militaria_and_related_items.knife_sheaths.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2296": {
        OfferCategory.antiques_and_collectibles.value(),
        OfferCategory.antiques_and_collectibles.militaria_and_related_items.value(),
        OfferCategory.antiques_and_collectibles.militaria_and_related_items.tactical_gear.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB4377": {
        OfferCategory.games.value(),
        OfferCategory.games.console_accessories.value(),
        OfferCategory.games.console_accessories.for_nintendo.value(),
        OfferCategory.games.console_accessories.for_nintendo.nintendo_64.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB271448": {
        OfferCategory.games.console_accessories.for_nintendo.nintendo_switch.cases_and_sleeves.value(),
        OfferCategory.games.console_accessories.for_nintendo.nintendo_switch.value(),
        OfferCategory.games.console_accessories.for_nintendo.value(),
        OfferCategory.games.console_accessories.value(),
        OfferCategory.games.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB272187": {
        OfferCategory.games.value(),
        OfferCategory.games.console_accessories.value(),
        OfferCategory.games.console_accessories.for_nintendo.value(),
        OfferCategory.games.console_accessories.for_nintendo.nintendo_switch.value(),
        OfferCategory.games.console_accessories.for_nintendo.nintendo_switch.gamepads_and_joysticks.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB38536": {
        OfferCategory.games.value(),
        OfferCategory.games.console_accessories.value(),
        OfferCategory.games.console_accessories.for_playstation.value(),
        OfferCategory.games.console_accessories.for_playstation.playstation_3.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB277786": {
        OfferCategory.games.value(),
        OfferCategory.games.console_accessories.value(),
        OfferCategory.games.console_accessories.for_playstation.value(),
        OfferCategory.games.console_accessories.for_playstation.playstation_4.value(),
        OfferCategory.games.console_accessories.for_playstation.playstation_4.bases_and_supports.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB118902": {
        OfferCategory.games.value(),
        OfferCategory.games.console_accessories.value(),
        OfferCategory.games.console_accessories.for_playstation.value(),
        OfferCategory.games.console_accessories.for_playstation.playstation_4.value(),
        OfferCategory.games.console_accessories.for_playstation.playstation_4.gamepads_and_joysticks.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB439072": {
        OfferCategory.games.value(),
        OfferCategory.games.console_accessories.value(),
        OfferCategory.games.console_accessories.for_playstation.value(),
        OfferCategory.games.console_accessories.for_playstation.playstation_4.value(),
        OfferCategory.games.console_accessories.for_playstation.playstation_4.audio_and_video_for_gaming.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB455274": {
        OfferCategory.games.value(),
        OfferCategory.games.console_accessories.value(),
        OfferCategory.games.console_accessories.for_playstation.value(),
        OfferCategory.games.console_accessories.for_playstation.playstation_5.value(),
        OfferCategory.games.console_accessories.for_playstation.playstation_5.controller_charges.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB455268": {
        OfferCategory.games.value(),
        OfferCategory.games.console_accessories.value(),
        OfferCategory.games.console_accessories.for_playstation.value(),
        OfferCategory.games.console_accessories.for_playstation.playstation_5.value(),
        OfferCategory.games.console_accessories.for_playstation.playstation_5.controller_cases.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB455266": {
        OfferCategory.games.value(),
        OfferCategory.games.console_accessories.value(),
        OfferCategory.games.console_accessories.for_playstation.value(),
        OfferCategory.games.console_accessories.for_playstation.playstation_5.value(),
        OfferCategory.games.console_accessories.for_playstation.playstation_5.gamepads_and_joysticks.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB455412": {
        OfferCategory.games.value(),
        OfferCategory.games.console_accessories.value(),
        OfferCategory.games.console_accessories.for_playstation.value(),
        OfferCategory.games.console_accessories.for_playstation.playstation_5.value(),
        OfferCategory.games.console_accessories.for_playstation.playstation_5.audio_and_video_for_gaming.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB5189": {
        OfferCategory.games.value(),
        OfferCategory.games.console_accessories.value(),
        OfferCategory.games.console_accessories.playstation_2.value(),
        OfferCategory.games.console_accessories.playstation_2.memory_cards.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB414209": {
        OfferCategory.games.value(),
        OfferCategory.games.console_accessories.value(),
        OfferCategory.games.console_accessories.playstation_2.value(),
        OfferCategory.games.console_accessories.playstation_2.microphones.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB439598": {
        OfferCategory.games.value(),
        OfferCategory.games.pc_gaming_accessories.value(),
        OfferCategory.games.pc_gaming_accessories.gaming_chairs.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB448169": {
        OfferCategory.games.value(),
        OfferCategory.games.pc_gaming_accessories.value(),
        OfferCategory.games.pc_gaming_accessories.controllers_and_joysticks.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB439596": {
        OfferCategory.games.value(),
        OfferCategory.games.pc_gaming_accessories.value(),
        OfferCategory.games.pc_gaming_accessories.headphones.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB439599": {
        OfferCategory.games.value(),
        OfferCategory.games.pc_gaming_accessories.value(),
        OfferCategory.games.pc_gaming_accessories.microphones.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB439595": {
        OfferCategory.games.value(),
        OfferCategory.games.pc_gaming_accessories.value(),
        OfferCategory.games.pc_gaming_accessories.vr_headset.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB11172": {
        OfferCategory.games.value(),
        OfferCategory.games.consoles.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438638": {
        OfferCategory.games.value(),
        OfferCategory.games.console_parts.value(),
        OfferCategory.games.console_parts.for_playstation.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438637": {
        OfferCategory.games.value(),
        OfferCategory.games.console_parts.value(),
        OfferCategory.games.console_parts.for_xbox.value(),
    },
}


def add_promotion_type_to_url(
    url: str, promotion_type: Literal["deal_of_the_day", "lightning"]
) -> str:
    if "?" in url:
        return url + f"&promotion_type={promotion_type}"
    return url + f"?promotion_type={promotion_type}"


async def extract_price(locator: Locator) -> dict[str, int]:
    if await locator.count() > 0:
        price: dict[str, int] = {}
        locator_attribute = await locator.get_attribute("aria-label")
        if locator_attribute is None:
            raise
        price["reais"] = int(
            locator_attribute[
                locator_attribute.index(": ")
                + len(": ") : locator_attribute.index(" reais") :
            ]
        )
        if locator_attribute.count("centavos") == 1:
            price["cents"] = int(
                locator_attribute[
                    locator_attribute.index("com ")
                    + len("com ") : locator_attribute.index("centavos") :
                ]
            )
        else:
            price["cents"] = 0
        return price
    raise RuntimeError("Price not found")


async def extract_title(locator: Locator) -> str:
    if await locator.count() > 0:
        return await locator.inner_text()
    raise RuntimeError("Title not found")


async def extract_rating(locator: Locator) -> float:
    if await locator.count() > 0:
        return float(await locator.inner_text())
    raise RuntimeError("Rating not found")


async def extract_url(locator: Locator) -> str:
    if await locator.count() > 0:
        url = await locator.get_attribute("href")
        if url is not None:
            return url
    raise RuntimeError("Product URL not found")


async def extract_image_url(locator: Locator) -> str:
    if await locator.count() > 0:
        url = await locator.first.get_attribute("src")
        if url is not None:
            return url
    raise RuntimeError("Image URL not found")


async def extract_total_reviews(locator: Locator) -> int:
    if await locator.count() > 0:
        return int((await locator.inner_text()).strip("()"))
    raise RuntimeError("Total reviews not found")


async def generate_countdown_timestamp(locator: Locator) -> datetime:
    if await locator.count() > 0:
        countdown_parts = ((await locator.inner_text()).replace("\n", "")).split(":")
        hours = (int(countdown_parts[0][0]) * 10) + int(countdown_parts[0][1])
        minutes = (int(countdown_parts[1][0]) * 10) + int(countdown_parts[1][1])
        seconds = (int(countdown_parts[2][0]) * 10) + int(countdown_parts[2][1])
        return datetime.now(tz=timezone.utc) + timedelta(
            hours=hours, minutes=minutes, seconds=seconds
        )
    raise RuntimeError("Countdown not found")


async def web_scraping_deals_of_the_day_products(
    page: Page,
) -> AsyncGenerator[DealOfTheDayProduct, None]:
    for url, categories in PRODUCTS_DEALS_BY_CATEGORIES.items():
        url = add_promotion_type_to_url(url=url, promotion_type="deal_of_the_day")
        await page.goto(url=url)
        has_next_page = True
        while has_next_page:
            products_locators = await page.locator(".poly-card").all()
            if len(products_locators) == 0:
                has_next_page = False
                continue
            for product_locator in products_locators:
                try:
                    product: dict[str, Any] = {"categories": categories}
                    locator = product_locator.locator(".poly-component__title")
                    product["title"] = await extract_title(locator=locator)
                    product["url"] = await extract_url(locator=locator)
                    locator = product_locator.locator("img")
                    product["image_url"] = await extract_image_url(locator=locator)
                    locator = product_locator.locator(".poly-reviews__rating")
                    product["rating"] = await extract_rating(locator=locator)
                    locator = product_locator.locator(".poly-reviews__total")
                    product["total_reviews"] = await extract_total_reviews(
                        locator=locator
                    )
                    locator = product_locator.locator(".andes-money-amount--previous")
                    product["old_price"] = await extract_price(locator=locator)
                    locator = product_locator.locator(
                        ".poly-price__current .andes-money-amount"
                    )
                    product["current_price"] = await extract_price(locator=locator)
                    yield DealOfTheDayProduct(**product)
                except Exception:
                    continue
            next_button = page.locator(
                ".andes-pagination__button--next a, li.andes-pagination__button--next a"
            )
            if await next_button.count() > 0 and await next_button.is_visible():
                current_url = page.url
                await next_button.click()
                if page.url == current_url:
                    has_next_page = False
            else:
                has_next_page = False


async def web_scraping_lightning_deals_products(
    page: Page,
) -> AsyncGenerator[LightningDealProduct, None]:
    for url, categories in PRODUCTS_DEALS_BY_CATEGORIES.items():
        url = add_promotion_type_to_url(url=url, promotion_type="lightning")
        await page.goto(url=url)
        has_next_page = True
        while has_next_page:
            products_locators = await page.locator(".poly-card").all()
            if len(products_locators) == 0:
                has_next_page = False
                continue
            for product_locator in products_locators:
                try:
                    product: dict[str, Any] = {"categories": categories}
                    locator = product_locator.locator(".poly-component__countdown")
                    product["expires_in"] = await generate_countdown_timestamp(
                        locator=locator
                    )
                    locator = product_locator.locator(".poly-component__title")
                    product["title"] = await extract_title(locator=locator)
                    product["url"] = await extract_url(locator=locator)
                    locator = product_locator.locator("img")
                    product["image_url"] = await extract_image_url(locator=locator)
                    locator = product_locator.locator(".poly-reviews__rating")
                    product["rating"] = await extract_rating(locator=locator)
                    locator = product_locator.locator(".poly-reviews__total")
                    product["total_reviews"] = await extract_total_reviews(
                        locator=locator
                    )
                    locator = product_locator.locator(".andes-money-amount--previous")
                    product["old_price"] = await extract_price(locator=locator)
                    locator = product_locator.locator(
                        ".poly-price__current .andes-money-amount"
                    )
                    product["current_price"] = await extract_price(locator=locator)
                    yield LightningDealProduct(**product)
                except Exception:
                    continue
            next_button = page.locator(
                ".andes-pagination__button--next a, li.andes-pagination__button--next a"
            )
            if await next_button.count() > 0 and await next_button.is_visible():
                current_url = page.url
                await next_button.click()
                if page.url == current_url:
                    has_next_page = False
            else:
                has_next_page = False
