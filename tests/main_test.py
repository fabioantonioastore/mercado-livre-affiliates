import asyncio
import os

import dotenv
from mercado_livre_affiliates import MercadoLivreAffiliates

dotenv.load_dotenv()
APP_PASSWORD = str(os.getenv("APP_PASSWORD"))


async def main() -> None:
    async with MercadoLivreAffiliates() as mercado_livre_affiliates:
        async with mercado_livre_affiliates.create_session(
            gmail_address="astore.a.fabio@gmail.com", app_password=APP_PASSWORD
        ) as session:
            await session.manual_login()
            print(
                await session.generate_affiliate_link(
                    product_url="https://produto.mercadolivre.com.br/MLB-3806655487-tnis-flyer-runner-mesh-bdp-puma-_JM#reco_item_pos=1&reco_backend=item_decorator&reco_backend_type=function&reco_client=home_items-decorator-legacy&reco_id=b5a34250-79b0-4cc3-b1b6-705f5dd7c5ee&reco_model=&c_id=/home/bookmarks-recommendations-seed/element&c_uid=a1e55870-0ce5-4773-84be-e4b8d50fa6c3&da_id=bookmark&da_position=1&id_origin=/home/dynamic_access&da_sort_algorithm=ranker"
                )
            )


asyncio.run(main=main())
