import re
from typing import Any
from asyncio import sleep

from playwright.async_api import async_playwright, BrowserContext, Page

from .imap import GmailClient
from .utils import fetch_last_email_content, extract_verification_code_from_email
from .errors import LoginError, ChromiumLaunchError

LOGIN_URL = "https://www.mercadolivre.com/jms/mlb/lgz/msl/login"
LINK_BUILDER_URL = "https://www.mercadolivre.com.br/afiliados/linkbuilder"
AFFILIATE_HUB_URL = "https://www.mercadolivre.com.br/afiliados/hub"


class MercadoLivreAffiliates:
    def __init__(self, gmail: str, app_password: str) -> None:
        self.__playwright = None
        self.__context = None
        self.__gmail = gmail
        self.__app_password = app_password

    async def add_cookies(self, cookies: list[Any]) -> None:
        context = await self.__get_context()
        await context.add_cookies(cookies)

    async def manual_login(self) -> None:
        if self.__playwright is None:
            self.__playwright = await async_playwright().start()
        context = await self.__playwright.chromium.launch_persistent_context(
                user_data_dir="./profile",
                headless=False,
                args=["--disable-blink-features=AutomationControlled"],
                user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
                locale="pt-BR",
                timezone_id="America/Sao_Paulo",
                viewport={"width": 1280, "height": 720},
            )
        page = await context.new_page()
        await page.goto(LOGIN_URL)
        await page.pause()
        await context.close()

    async def __get_context(self) -> BrowserContext:
        if isinstance(self.__context, BrowserContext):
            return self.__context
        if self.__playwright is None:
            self.__playwright = await async_playwright().start()
        try:
            self.__context = await self.__playwright.chromium.launch_persistent_context(
                user_data_dir="./profile",
                headless=True,
                args=["--disable-blink-features=AutomationControlled"],
                user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
                locale="pt-BR",
                timezone_id="America/Sao_Paulo",
                viewport={"width": 1280, "height": 720},
            )
            return self.__context
        except Exception:
            raise ChromiumLaunchError("Execute: playwrigh install chromium")

    async def __is_logged(self, page: Page | None = None) -> bool:
        created_page = False
        if page is None:
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
        if page is None:
            page = await context.new_page()
            created_page = True
        try:
            async with GmailClient(self.__gmail, self.__app_password) as gmail_client:
                await page.goto(url=LOGIN_URL)
                email_input = page.get_by_role(
                    role="textbox", name="E-mail ou telefone"
                )
                await email_input.wait_for(state="visible")
                await email_input.fill(value=self.__gmail)
                continue_button = page.get_by_role(role="button", name="Continuar")
                await continue_button.wait_for(state="visible")
                await continue_button.click()
                email_verification_option = page.get_by_role(
                    role="button", name="E-mail Vamos enviar um código"
                )
                await email_verification_option.wait_for(state="visible")
                await email_verification_option.click()
                await sleep(10)
                email_content = await fetch_last_email_content(gmail_client)
                if email_content is None:
                    raise LoginError("Not content email fetched")
                verification_code = extract_verification_code_from_email(email_content)
                if verification_code is None:
                    raise LoginError("Not verification code extracted")
                for i in range(len(verification_code)):
                    digit_input = page.get_by_role(
                        role="textbox", name=f"Dígito {i + 1}"
                    )
                    await digit_input.wait_for(state="visible")
                    await digit_input.fill(verification_code[i])
                submit_button = page.get_by_test_id(test_id="submit-button")
                await submit_button.wait_for(state="visible")
                await submit_button.click()
        except Exception:
            raise LoginError("A error occurs during login")
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
        if self.__context:
            await self.__context.close()
        if self.__playwright:
            await self.__playwright.stop()

    def __repr__(self) -> str:
        return "MercadoLivreAffiliates()"
