import re
from typing import Any

from playwright.async_api import async_playwright, BrowserContext


LINK_BUILDER_URL = "https://www.mercadolivre.com.br/afiliados/linkbuilder"


class MercadoLivreAffiliates:
    def __init__(self, headless: bool = False) -> None:
        self.__playwright = None
        self._headless = headless
        self._context = None

    async def _get_persistent_context(self) -> BrowserContext:
        if isinstance(self._context, BrowserContext):
            return self._context
        if self.__playwright is None:
            self.__playwright = await async_playwright().start()
        self._context = await self.__playwright.chromium.launch_persistent_context(
            user_data_dir="./profile",
            headless=self._headless
        )
        return self._context
    
    async def _add_cookies(self, cookies: list[Any]) -> None:
        context = await self._get_persistent_context()
        await context.add_cookies(cookies)
    
    async def auth(self, cookies: list[Any]) -> None:
        await self._add_cookies(cookies)
    
    async def close(self) -> None:
        if self._context:
            await self._context.close()
        if self.__playwright:
            await self.__playwright.stop()

    async def generate_affiliate_link(self, product_url: str) -> str | None:
        context = await self._get_persistent_context()
        page = await context.new_page()
        await page.goto(LINK_BUILDER_URL, wait_until="domcontentloaded")
        if self._headless:
            pass
        url_input = page.get_by_role("textbox", name="Insira 1 ou mais URLs separados por 1 linha")
        await url_input.wait_for()
        await url_input.type(product_url, delay=100)
        generate_button = page.get_by_role("button", name="Gerar")
        await generate_button.click()
        link_element = page.get_by_text(re.compile(r"^https://"))
        await link_element.wait_for()
        return await link_element.text_content()

    def __repr__(self) -> str:
        return "MercadoLivreAffiliates()"
