from typing import AsyncGenerator, Any, Literal
from datetime import datetime, timedelta, timezone

from playwright.async_api import Page, Locator

from .._models import DealOfTheDayProduct, LightningDealProduct
from ..enums import OfferCategory

PRODUCTS_DEALS_BY_CATEGORIES: dict[str, set[str]] = {
    "https://www.mercadolivre.com.br/ofertas?category=MLB1747": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.CAR_AND_PICKUP_TRUCK_ACCESSORIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1771": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.MOTORCYCLE_AND_ATV_ACCESSORIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB6005": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.MARINE_ACCESSORIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB438364": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.HEAVY_DUTY_ACCESSORIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2227": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.VEHICLE_TOOLS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB188063": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.AUTOMOTIVE_CLEANING.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB456111": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.LUBRICANTS_AND_FLUIDS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB8531": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.GPS_NAVIGATORS_FOR_VEHICLES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB260634": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.PERFORMANCE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB456046": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.MARINE_PARTS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB22693": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.CAR_AND_PICKUP_TRUCK_PARTS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB419936": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.HEAVY_DUTY_PARTS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB243551": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.MOTORCYCLE_AND_ATV_PARTS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2238": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.TIRES_AND_ACCESSORIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB255788": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.WHEELS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2239": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.VEHICLE_SAFETY.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB3381": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.CAR_AUDIO.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1776": {
        OfferCategory.VEHICLE_ACCESSORIES.value(),
        OfferCategory.VEHICLE_ACCESSORIES.TUNING.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB456826": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.BEEKEEPING.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB456820": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.STORAGE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB456833": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.RENEWABLE_ENERGY.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB456927": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.WORK_TOOLS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB454448": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.RURAL_INFRASTRUCTURE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB442343": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.AGRICULTURAL_INPUTS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB271641": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.LIVESTOCK_SUPPLIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1514": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.AGRICULTURAL_MACHINERY.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB442351": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.AGRICULTURAL_MACHINERY_PARTS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB457052": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.ANIMAL_PRODUCTION.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB456795": {
        OfferCategory.AGRIBUSINESS.value(),
        OfferCategory.AGRIBUSINESS.CROP_PROTECTION.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB278123": {
        OfferCategory.FOOD_AND_BEVERAGE.value(),
        OfferCategory.FOOD_AND_BEVERAGE.BEVERAGES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB410883": {
        OfferCategory.FOOD_AND_BEVERAGE.value(),
        OfferCategory.FOOD_AND_BEVERAGE.PREPARED_FOOD.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB439739": {
        OfferCategory.FOOD_AND_BEVERAGE.value(),
        OfferCategory.FOOD_AND_BEVERAGE.FRESH.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB455505": {
        OfferCategory.FOOD_AND_BEVERAGE.value(),
        OfferCategory.FOOD_AND_BEVERAGE.KEFIR.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1423": {
        OfferCategory.FOOD_AND_BEVERAGE.value(),
        OfferCategory.FOOD_AND_BEVERAGE.GROCERY_STORE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB436789": {
        OfferCategory.ANTIQUES_AND_COLLECTIBLES.value(),
        OfferCategory.ANTIQUES_AND_COLLECTIBLES.ANTIQUES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB393901": {
        OfferCategory.ANTIQUES_AND_COLLECTIBLES.value(),
        OfferCategory.ANTIQUES_AND_COLLECTIBLES.FLAGS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1806": {
        OfferCategory.ANTIQUES_AND_COLLECTIBLES.value(),
        OfferCategory.ANTIQUES_AND_COLLECTIBLES.BANKNOTES_AND_COINS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2662": {
        OfferCategory.ANTIQUES_AND_COLLECTIBLES.value(),
        OfferCategory.ANTIQUES_AND_COLLECTIBLES.SCULPTURES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1369": {
        OfferCategory.ART_SUPPLIES_STATIONERY_AND_HABERDASHERY.value(),
        OfferCategory.ART_SUPPLIES_STATIONERY_AND_HABERDASHERY.ART_AND_CRAFTS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB270263": {
        OfferCategory.ART_SUPPLIES_STATIONERY_AND_HABERDASHERY.value(),
        OfferCategory.ART_SUPPLIES_STATIONERY_AND_HABERDASHERY.HABERDASHERY_SUPPLIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB44011": {
        OfferCategory.ART_SUPPLIES_STATIONERY_AND_HABERDASHERY.value(),
        OfferCategory.ART_SUPPLIES_STATIONERY_AND_HABERDASHERY.SCHOOL_SUPPLIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB5360": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.NUTRITION_AND_BREASTFEEDING.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB420332": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.WALKERS_AND_RIDE_ON_TOYS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB420334": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.BABYS_BATH.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1392": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.BABY_TOYS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB40563": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.PLAYPEN.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB420293": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.PACIFIERS_AND_TEETHERS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB420375": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.BABY_HYGIENE_AND_CARE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB420295": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.MATERNITY.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB420409": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.BABY_STROLL.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB420361": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.BABYS_ROOM.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1396": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.BABY_CLOTHES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB420353": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.BABYS_HEALTH.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB5358": {
        OfferCategory.BABIES.value(),
        OfferCategory.BABIES.BABY_SAFETY.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB455174": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.HAIR_ACCESSORIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB264751": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.HAIRDRESSING_SUPPLIES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB264787": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.BARBERSHOP.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB199407": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.SKINCARE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1263": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.HAIR_CARE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB5383": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.HAIR_REMOVAL.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB431646": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.PHARMACY.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB198312": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.PERSONAL_HYGIENE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB29884": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.MANICURE_AND_PEDICURE.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1248": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.MAKEUP.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB6284": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.PERFUMES.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB278194": {
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.value(),
        OfferCategory.BEAUTY_AND_PERSONAL_CARE.BEAUTY_TREATMENTS.value(),
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB432991": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.ANTI_STRESS_AND_INGENUITY.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB6911": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.OUTDOORS_AND_PLAYGROUND.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1132": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.ARTS_AND_ACTIVITIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB264337": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.DOLLS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB2961": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.ELECTRONIC_TOYS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB432818": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.PRETEND_PLAY_TOYS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB455425": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.BUILDING_TOYS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB433069": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.BEACH_AND_POOL_TOYS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB3655": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.BABY_TOYS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB433060": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.PLAYHOUSES_AND_PLAY_TENTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB433047": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.HAND_PUPPETS_AND_MARIONETTES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB432873": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.HOBBIES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB11229": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.MUSICAL_INSTRUMENTS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB437648": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.PARLOR_GAMES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB432988": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.BOARD_AND_CARD_GAMES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB255050": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.TOY_LAUNCHERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB270072": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.TABLES_AND_CHAIRS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB6905": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.MINI_VEHICLES_AND_BICYCLES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1910": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.OTHERS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1166": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.PLUSH_TOYS.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB432871": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.TOY_VEHICLES.value()
    },
    "https://www.mercadolivre.com.br/ofertas?category=MLB1831": {
        OfferCategory.TOYS_AND_HOBBIES.value(),
        OfferCategory.TOYS_AND_HOBBIES.ALBUMS_AND_STICKERS.value()
    }
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
