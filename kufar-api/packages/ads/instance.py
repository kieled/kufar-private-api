from base import BaseService

from . import consts
from .schemas import (
    GetAdvertByListIdResponse,
    GetAdvertResponse,
    GetPhoneResponse,
    GetUserSearchAdvertsResponse,
)


class AdsService(BaseService):
    async def get_advert(self, ad_id: int, lang: str = 'ru') -> GetAdvertResponse:
        return await self.client.get(
            consts.GET_ADVERT.format(ad_id=ad_id),
            headers=consts.SEGMENTATION_HEADER,
            params={'lang': lang}
        )

    async def get_advert_by_list_id(self, msgi: str, size: str, lang: str = 'ru') -> GetAdvertByListIdResponse:
        return await self.client.get(
            consts.SEARCH_ADVERTS,
            headers=consts.SEGMENTATION_HEADER_WITH_HACK,
            params={
                'msgi': msgi,
                'size': size,
                'lang': lang
            }
        )

    async def get_ad_phone(self, ad_id: int) -> GetPhoneResponse:
        return await self.client.get(consts.GET_PHONE.format(ad_id=ad_id))

    async def user_search_adverts(self, size: int, cursor: str | None = None) -> GetUserSearchAdvertsResponse:
        return await self.client.get(
            consts.SEARCH_ADVERTS,
            headers=consts.USER_SEGMENTATION_HEADER,
            params={
                'size': size,
                'cursor': cursor
            }
        )
