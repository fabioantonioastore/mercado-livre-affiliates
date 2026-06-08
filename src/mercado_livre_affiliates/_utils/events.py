from typing import AsyncGenerator, Any
from datetime import datetime, timedelta, timezone

from playwright.async_api import Page, Locator

from .._models import DealOfTheDayProduct, LightningDealProduct

DAY_OFFERS_URL = (
    "https://www.mercadolivre.com.br/ofertas?promotion_type=deal_of_the_day"
)
LIGHTNING_OFFERS_URL = "https://www.mercadolivre.com.br/ofertas?promotion_type=lightning"


async def extract_product_price_from_locator(locator: Locator) -> dict[str, int]:
    price: dict[str, int] = {}
    locator_attribute = await locator.get_attribute("aria-label")
    if locator_attribute is None:
        raise
    price["reais"] = int(
        locator_attribute[
            locator_attribute.index(": ") + len(": ") : locator_attribute.index(" reais") :
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


async def generate_timestamp_from_lightning_deal_countdown_locator(locator: Locator) -> datetime:
    countdown_parts = ((await locator.inner_text()).replace("\n", "")).split(":")
    hours = (int(countdown_parts[0][0]) * 10) + int(countdown_parts[0][1])
    minutes = (int(countdown_parts[1][0]) * 10) + int(countdown_parts[1][1])
    seconds = (int(countdown_parts[2][0]) * 10) + int(countdown_parts[2][1])
    return datetime.now(tz=timezone.utc) + timedelta(hours=hours, minutes=minutes, seconds=seconds)


async def web_scraping_deals_of_the_day_products(
    page: Page,
) -> AsyncGenerator[DealOfTheDayProduct, None]:
    await page.goto(url=DAY_OFFERS_URL)
    has_next_page = True
    while has_next_page:
        await page.wait_for_selector(".poly-card")
        for _ in range(5):
            await page.evaluate("window.scrollBy(0, window.innerHeight);")
            await page.wait_for_timeout(timeout=400)
        products_locators = await page.locator(".poly-card").all()
        for product_locator in products_locators:
            try:
                product: dict[str, Any] = {}
                locator = product_locator.locator(".poly-component__title")
                product["title"] = await locator.inner_text()
                product["url"] = await locator.get_attribute("href")
                locator = product_locator.locator("img")
                product["image_url"] = await locator.first.get_attribute("src")
                locator = product_locator.locator(".poly-reviews__rating")
                product["rating"] = float(await locator.inner_text())
                locator = product_locator.locator(".poly-reviews__total")
                product["total_reviews"] = int((await locator.inner_text()).strip("()"))
                locator = product_locator.locator(".andes-money-amount--previous")
                product["old_price"] = await extract_product_price_from_locator(locator=locator)
                locator = product_locator.locator(
                    ".poly-price__current .andes-money-amount"
                )
                product["current_price"] = await extract_product_price_from_locator(locator=locator)
                locator = product_locator.locator(".poly-price__disc_label")
                discount = await locator.inner_text()
                discount = float(discount[0 : discount.index("%") :]) / 100
                product["discount_factor"] = discount
                yield DealOfTheDayProduct(**product)
            except Exception:
                continue
        next_button = page.locator(
            ".andes-pagination__button--next a, li.andes-pagination__button--next a"
        )
        if await next_button.count() > 0 and await next_button.is_visible():
            current_url = page.url
            await next_button.click()
            await page.wait_for_timeout(2000)
            if page.url == current_url:
                has_next_page = False
        else:
            has_next_page = False


async def web_scraping_lightning_deals_products(page: Page) -> AsyncGenerator[LightningDealProduct, None]:
    await page.goto(url=LIGHTNING_OFFERS_URL)
    has_next_page = True
    while has_next_page:
        await page.wait_for_selector(".poly-card")
        for _ in range(5):
            await page.evaluate("window.scrollBy(0, window.innerHeight);")
            await page.wait_for_timeout(timeout=400)
        products_locators = await page.locator(".poly-card").all()
        for product_locator in products_locators:
            try:
                product: dict[str, Any] = {}
                locator = product_locator.locator(".poly-component__countdown")
                product["expires_in"] = await generate_timestamp_from_lightning_deal_countdown_locator(locator=locator)
                locator = product_locator.locator(".poly-component__title")
                product["title"] = await locator.inner_text()
                product["url"] = await locator.get_attribute("href")
                locator = product_locator.locator("img")
                product["image_url"] = await locator.first.get_attribute("src")
                locator = product_locator.locator(".poly-reviews__rating")
                product["rating"] = float(await locator.inner_text())
                locator = product_locator.locator(".poly-reviews__total")
                product["total_reviews"] = int((await locator.inner_text()).strip("()"))
                locator = product_locator.locator(".andes-money-amount--previous")
                product["old_price"] = await extract_product_price_from_locator(locator=locator)
                locator = product_locator.locator(
                    ".poly-price__current .andes-money-amount"
                )
                product["current_price"] = await extract_product_price_from_locator(locator=locator)
                locator = product_locator.locator(".poly-price__disc_label")
                discount = await locator.inner_text()
                discount = float(discount[0 : discount.index("%") :]) / 100
                product["discount_factor"] = discount
                yield LightningDealProduct(**product)
            except Exception:
                continue
        next_button = page.locator(
            ".andes-pagination__button--next a, li.andes-pagination__button--next a"
        )
        if await next_button.count() > 0 and await next_button.is_visible():
            current_url = page.url
            await next_button.click()
            await page.wait_for_timeout(2000)
            if page.url == current_url:
                has_next_page = False
        else:
            has_next_page = False
