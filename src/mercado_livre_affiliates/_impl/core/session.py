import re
import asyncio
from uuid import uuid4, UUID
from contextlib import AbstractAsyncContextManager
from types import TracebackType

from playwright.async_api import BrowserContext, Page, async_playwright

from ..services import Gmail
from ..exceptions import IsSessionLoggedError, LoginError, GenerateAffiliateLinkError
from ..utils.mercado_livre_affiliates import (
    extract_mercado_livre_verification_code_from_mail,
)

LOGIN_URL = "https://www.mercadolivre.com/jms/mlb/lgz/msl/login"
AFFILIATE_HUB_URL = "https://www.mercadolivre.com.br/afiliados/hub"
LINK_BUILDER_URL = "https://www.mercadolivre.com.br/afiliados/linkbuilder"


class MercadoLivreAffiliatesSession(
    AbstractAsyncContextManager["MercadoLivreAffiliatesSession"]
):
    def __init__(
        self, gmail_address: str, app_password: str, browser_context: BrowserContext
    ) -> None:
        self.__gmail_address = gmail_address
        self.__app_password = app_password
        self.__browser_context = browser_context
        self.__uuid = uuid4()

    @property
    def uuid(self) -> UUID:
        return self.__uuid

    @property
    def gmail_address(self) -> str:
        return self.__gmail_address

    async def close(self) -> None:
        if not self.__browser_context.is_closed():
            await self.__browser_context.close()

    async def is_logged(self, page: Page | None = None) -> bool:
        create_page = False
        if page is None:
            page = await self.__browser_context.new_page()
            create_page = True
        try:
            await page.goto(url=AFFILIATE_HUB_URL)
            return "login" not in page.url.lower()
        except Exception as error:
            raise IsSessionLoggedError(
                f"Failed on verify if session is logged: {error}"
            )
        finally:
            if create_page:
                await page.close()

    async def login(self, page: Page | None = None) -> None:
        created_page = False
        if page is None:
            page = await self.__browser_context.new_page()
        try:
            async with Gmail(
                gmail_address=self.gmail_address, app_password=self.__app_password
            ) as gmail:
                await page.goto(url=LOGIN_URL)
                email_input = page.get_by_role(
                    role="textbox", name="E-mail ou telefone"
                )
                await email_input.wait_for(state="visible")
                await email_input.fill(value=self.gmail_address)
                continue_button = page.get_by_role(role="button", name="Continuar")
                await continue_button.wait_for(state="visible")
                await continue_button.click()
                email_verification_option_input = page.get_by_role(
                    role="button", name="E-mail Vamos enviar um código"
                )
                await email_verification_option_input.wait_for(state="visible")
                await email_verification_option_input.click()
                await asyncio.sleep(10)
                email_content = await gmail.fetch_last_sender_mail_content(
                    sender="Mercado Livre"
                )
                if email_content is None:
                    raise LoginError("Not email fetched")
                verification_code = extract_mercado_livre_verification_code_from_mail(
                    mail_content=email_content
                )
                if verification_code is None:
                    raise LoginError("Not verification code extracted")
                for i in range(len(verification_code)):
                    digit_input = page.get_by_role(
                        role="textbox", name=f"Dígito {i + 1}"
                    )
                    await digit_input.wait_for(state="visible")
                    await digit_input.fill(verification_code[i])
                submit_button_input = page.get_by_test_id(test_id="submit-button")
                await submit_button_input.wait_for(state="visible")
                await submit_button_input.click()
                await asyncio.sleep(5)
        except Exception as error:
            raise LoginError(f"Failed to make login: {error}")
        finally:
            if created_page:
                await page.close()

    async def manual_login(self) -> None:
        playwright = await async_playwright().start()
        browser = await playwright.chromium.launch(
            headless=False, args=["--disable-blink-features=AutomationControlled"]
        )
        browser_context = await browser.new_context(
            user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
            locale="pt-BR",
            timezone_id="America/Sao_Paulo",
            viewport={"width": 1280, "height": 720},
        )
        page = await browser_context.new_page()
        try:
            await page.goto(LOGIN_URL)
            await page.pause()
            await asyncio.sleep(5)
            await self.__browser_context.add_cookies(cookies=await browser_context.cookies())  # type: ignore
        except Exception as error:
            raise LoginError(f"Failed to make manual login: {error}")
        finally:
            await page.close()
            await browser_context.close()
            await browser.close()
            await playwright.stop()

    async def generate_affiliate_link(self, product_url: str) -> str:
        page = await self.__browser_context.new_page()
        if not await self.is_logged(page=page):
            await self.login()
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
            link = await link_element.first.text_content()
            if link is None:
                raise GenerateAffiliateLinkError("Failed to generate affiliate link")
            return link
        except Exception as error:
            raise GenerateAffiliateLinkError(
                f"Failed to generate affiliate link: {error}"
            )
        finally:
            await page.close()

    async def __aenter__(self) -> "MercadoLivreAffiliatesSession":
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        await self.close()
