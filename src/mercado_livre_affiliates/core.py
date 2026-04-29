import re
from asyncio import Lock

from playwright.async_api import async_playwright, BrowserContext, Page
from playwright._impl._errors import Error

from imap import GmailClient


LOGIN_URL = "https://www.mercadolivre.com/jms/mlb/lgz/msl/login"
LINK_BUILDER_URL = "https://www.mercadolivre.com.br/afiliados/linkbuilder"
AFFILIATE_HUB_URL = "https://www.mercadolivre.com.br/afiliados/hub"


class MercadoLivreAffiliates:
    def __init__(self, gmail: str, app_password: str) -> None:
        self.__playwright = None
        self._context = None
        self._gmail_client = GmailClient(gmail, app_password)
        self._lock = Lock()

    async def __get_context(self) -> BrowserContext:
        async with self._lock:
            if isinstance(self._context, BrowserContext):
                return self._context
            if self.__playwright is None:
                self.__playwright = await async_playwright().start()
            try:
                self._context = await self.__playwright.chromium.launch_persistent_context(
                    user_data_dir="./profile",
                    headless=False,
                    args=["--disable-blink-features=AutomationControlled"],
                    user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
                    locale="pt-BR",
                )
                return self._context
            except Error:
                raise RuntimeError("Execute: playwrigh install chromium")

    async def __is_logged(self, page: Page | None = None) -> bool:
        created_page = False
        if not page:
            context = await self.__get_context()
            page = await context.new_page()
            created_page = True
        try:
            await page.goto(url=AFFILIATE_HUB_URL)
            return "login" not in page.url.lower()
        finally:
            if created_page:
                await page.close()

    async def __login(self, page: Page | None = None) -> None:
        created_page = False
        context = await self.__get_context()
        if not page:
            page = await context.new_page()
            created_page = True
        try:
            await page.goto(url=LOGIN_URL)
            email_input = page.get_by_role(role="textbox", name="E-mail ou telefone")
            await email_input.wait_for(state="visible")
            await email_input.fill(value=self._gmail_client.gmail)
            continue_button = page.get_by_role(role="button", name="Continuar")
            await continue_button.wait_for(state="visible")
            await continue_button.click()
            email_verification_option = page.get_by_role(role="button", name="E-mail Vamos enviar um código")
            await email_verification_option.wait_for(state="visible")
            await email_verification_option.click()
        finally:
            if created_page:
                await page.close()

    async def generate_affiliate_link(self, product_url: str) -> str | None:
        context = await self.__get_context()
        page = await context.new_page()
        if not await self.__is_logged(page=page):
            await self.__login(page=page)
        try:
            await page.goto(LINK_BUILDER_URL, wait_until="networkidle")
            url_input = page.get_by_role(
                role="textbox", name="Insira 1 ou mais URLs separados por 1 linha"
            )
            await url_input.wait_for(state="visible")
            await url_input.fill(value=product_url)
            generate_button = page.get_by_role(role="button", name="Gerar")
            await generate_button.click()
            link_element = page.get_by_text(re.compile(r"^https://"))
            await link_element.wait_for(state="visible")
            return await link_element.first.text_content()
        finally:
            await page.close()

    async def close(self) -> None:
        if self._context:
            await self._context.close()
        if self.__playwright:
            await self.__playwright.stop()
        if self._gmail_client:
            await self._gmail_client.close()

    def __repr__(self) -> str:
        return "MercadoLivreAffiliates()"
