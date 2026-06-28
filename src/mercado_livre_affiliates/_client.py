import re
import asyncio
from contextlib import AbstractAsyncContextManager
from types import TracebackType
from typing import Self, Sequence, Callable, Coroutine, Any, overload

from playwright.async_api import (
    Playwright,
    BrowserContext,
    Page,
    Browser,
    Cookie,
    async_playwright,
)

from ._services import Gmail
from .exceptions import (
    IsLoggedError,
    LoginError,
    ManualLoginError,
    GenerateAffiliateLinkError,
)
from ._utils.client import extract_mercado_livre_verification_code_from_mail
from .events import DealsOfTheDay, LightningDeals
from ._models import EventResponse, DealOfTheDayProduct, LightningDealProduct

LOGIN_URL = "https://www.mercadolivre.com/jms/mlb/lgz/msl/login"
AFFILIATE_HUB_URL = "https://www.mercadolivre.com.br/afiliados/hub"
LINK_BUILDER_URL = "https://www.mercadolivre.com.br/afiliados/linkbuilder"


class MercadoLivreAffiliates(AbstractAsyncContextManager["MercadoLivreAffiliates"]):
    def __init__(self, browser: Browser | None = None) -> None:
        self.__gmail_address: str
        self.__app_password: str
        self.__playwright: Playwright | None = None
        self.__browser: Browser | None = browser
        self.__browser_context: BrowserContext | None = None
        self.__event_browser_context: BrowserContext | None = None
        self.__day_offers_event = DealsOfTheDay()
        self.__lightning_offers_event = LightningDeals()

    async def __aenter__(self) -> Self:
        await self.__start()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        await self.__stop()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    @overload
    async def register_event_function(
        self,
        event: type[DealsOfTheDay],
        function: Callable[
            ["MercadoLivreAffiliates", DealOfTheDayProduct], Coroutine[Any, Any, None]
        ],
    ) -> None: ...

    @overload
    async def register_event_function(
        self,
        event: type[LightningDeals],
        function: Callable[
            ["MercadoLivreAffiliates", LightningDealProduct], Coroutine[Any, Any, None]
        ],
    ) -> None: ...

    async def register_event_function(
        self,
        event: type[DealsOfTheDay] | type[LightningDeals],
        function: (
            Callable[
                ["MercadoLivreAffiliates", DealOfTheDayProduct],
                Coroutine[Any, Any, None],
            ]
            | Callable[
                ["MercadoLivreAffiliates", LightningDealProduct],
                Coroutine[Any, Any, None],
            ]
        ),
    ) -> None:
        if issubclass(event, DealsOfTheDay):
            self.__day_offers_event.register_event_function(function=function)  # type: ignore[arg-type]
            if not self.__day_offers_event.started:
                await self.__day_offers_event.start(client=self)
            return
        self.__lightning_offers_event.register_event_function(function=function)  # type: ignore[arg-type]
        if not self.__lightning_offers_event.started:
            await self.__lightning_offers_event.start(client=self)

    def set_user_account(self, gmail_address: str, app_password: str) -> None:
        self.__gmail_address = gmail_address
        self.__app_password = app_password

    async def remove_event_function(
        self,
        function: Callable[
            ["MercadoLivreAffiliates", EventResponse], Coroutine[Any, Any, None]
        ],
    ) -> None:
        self.__day_offers_event.remove_event_function(function=function)
        if self.__day_offers_event.total_event_functions == 0:
            await self.__day_offers_event.stop()
        self.__lightning_offers_event.remove_event_function(function=function)
        if self.__lightning_offers_event.total_event_functions == 0:
            await self.__lightning_offers_event.stop()

    async def add_cookies(self, cookies: Sequence[str]) -> None:
        await self.__browser_context.add_cookies(cookies=cookies)  # type: ignore

    async def get_cookies(self) -> list[Cookie]:
        browser_context = await self.__get_browser_context()
        return await browser_context.cookies()

    async def is_logged(self, page: Page | None = None) -> bool:
        create_page = False
        browser_context = await self.__get_browser_context()
        if page is None:
            page = await browser_context.new_page()
            create_page = True
        try:
            await page.goto(url=AFFILIATE_HUB_URL)
            return "login" not in page.url.lower()
        except Exception as error:
            raise IsLoggedError(f"Failed on verify if is logged: {error}")
        finally:
            if create_page:
                await page.close()

    async def login(self, page: Page | None = None) -> None:
        created_page = False
        browser_context = await self.__get_browser_context()
        if page is None:
            page = await browser_context.new_page()
        try:
            async with Gmail(
                gmail_address=self.__gmail_address, app_password=self.__app_password
            ) as gmail:
                await page.goto(url=LOGIN_URL)
                email_input = page.get_by_role(
                    role="textbox", name="E-mail ou telefone"
                )
                await email_input.wait_for(state="visible")
                await email_input.fill(value=self.__gmail_address)
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
            await (await self.__get_browser_context()).add_cookies(cookies=await browser_context.cookies())  # type: ignore
        except Exception as error:
            raise ManualLoginError(f"Failed to make manual login: {error}")
        finally:
            await page.close()
            await browser_context.close()
            await browser.close()
            await playwright.stop()

    async def generate_affiliate_link(self, product_url: str) -> str:
        browser_context = await self.__get_browser_context()
        page = await browser_context.new_page()
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

    async def _get_event_browser_context(self) -> BrowserContext:
        if self.__event_browser_context is None:
            self.__event_browser_context = await self.__create_event_browser_context()
        return self.__event_browser_context

    async def __create_event_browser_context(self) -> BrowserContext:
        if self.__event_browser_context is None:
            self.__event_browser_context = await self.__create_browser_context()
        return self.__event_browser_context

    async def __create_browser(self) -> Browser:
        playwright = await self.__get_playwright()
        return await playwright.chromium.launch(
            headless=True, args=["--disable-blink-features=AutomationControlled"]
        )

    async def __get_browser_context(self) -> BrowserContext:
        if self.__browser_context is None:
            self.__browser_context = await self.__create_browser_context()
        return self.__browser_context

    async def __create_browser_context(self) -> BrowserContext:
        if self.__browser is None:
            self.__browser = await self.__create_browser()
        return await self.__browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/637.36 Chrome/120 Safari/537.36",
            locale="pt-BR",
            timezone_id="America/Sao_Paulo",
        )

    async def __start(self) -> None:
        self.__playwright = await async_playwright().start()

    async def __stop(self) -> None:
        if self.__day_offers_event.started:
            await self.__day_offers_event.stop()
        if self.__lightning_offers_event.started:
            await self.__lightning_offers_event.stop()
        if (
            self.__event_browser_context is not None
            and not self.__event_browser_context.is_closed()
        ):
            await self.__event_browser_context.close()
        if (
            self.__browser_context is not None
            and not self.__browser_context.is_closed()
        ):
            await self.__browser_context.close()
        if self.__playwright is not None:
            await self.__playwright.stop()
        self.__event_browser_context = None
        self.__browser_context = None
        self.__playwright = None

    async def __get_playwright(self) -> Playwright:
        if self.__playwright is None:
            raise ValueError("Application not started yet")
        return self.__playwright
