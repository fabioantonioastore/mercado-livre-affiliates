from asyncio import run

from mercado_livre_affiliates import MercadoLivreAffiliates


async def main():
    mla = MercadoLivreAffiliates("sd", "adsfdf")
    await mla.manual_login()
    meli_url = "https://meli.la/2W7zi2K"
    final_product_url = await mla.get_meli_product_url(meli_url=meli_url)
    print(final_product_url)
    afflite_link = await mla.generate_affiliate_link(product_url=final_product_url)
    print(afflite_link)


run(main())
