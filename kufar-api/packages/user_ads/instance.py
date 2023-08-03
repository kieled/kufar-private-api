from base import BaseService
from utils.auth import auth_required

from . import consts
from .schemas import ModifyAdResponse, MyAdsCounterResponse, MyAdsResponse


class UserAdsService(BaseService):
    @auth_required
    async def get_counters(self):
        return await self.client.post_legacy(consts.GET_COUNTERS)
    
    @auth_required
    async def activate_ad(self, ad_id: int) -> ModifyAdResponse:
        return await self.client.post_legacy(consts.ACTIVATE_AD, params={
            'ad_id': ad_id
        })

    @auth_required
    async def delete_ad(self, ad_id: int) -> ModifyAdResponse:
        return await self.client.post_legacy(consts.DELETE_AD, params={
            'ad_id': ad_id
        })

    @auth_required
    async def get_my_ads(self, offset: int, limit: int, status: str) -> MyAdsResponse:
        return await self.client.get_legacy(consts.GET_MY_ADS, params={
            'offset': offset,
            'limit': limit,
            'status': status,
            'stats': 1
        })


    @auth_required
    async def get_my_ads_count(self) -> MyAdsCounterResponse:
        return await self.client.get_legacy(consts.GET_MY_ADS_COUNT)

    @auth_required
    async def prolong_ad(self, ad_id: int) -> ModifyAdResponse:
        return await self.client.post_legacy(consts.PROLONG_AD, params={
            'ad_id': ad_id
        })
