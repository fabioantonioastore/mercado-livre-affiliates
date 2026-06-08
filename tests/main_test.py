import asyncio

from mercado_livre_affiliates import MercadoLivreAffiliates


async def main() -> None:
    async with MercadoLivreAffiliates(
        gmail_address="astore.a.fabio@gmail.com", app_password="test"
    ) as mercado_livre_affiliates:
        link = await mercado_livre_affiliates.generate_affiliate_link(
            product_url="https://www.mercadolivre.com.br/02-potes-do-colageno-tipo-ii-45mg-formula-exclusiva-para-a-articulaco-com-maxima-concentraco-e-biodisponibilidade-120-capsulas/p/MLB43296945?pdp_filters=item_id:MLB5806607246#is_advertising=true&searchVariation=MLB43296945&backend_model=search-backend&be_origin=fallback&position=1&search_layout=grid&type=pad&tracking_id=46defcc9-855d-4686-b836-1911406947a3&ad_domain=VQCATCORE_LST&ad_position=1&ad_click_id=NjcyYzI2YzItYWI1OS00NDNiLWE1ZGMtZGIzMzIzYjVmNzQ1"
        )
        print(link)


asyncio.run(main=main())
