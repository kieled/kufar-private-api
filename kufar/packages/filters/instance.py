from kufar.base.service import BaseService
from .schemas import MetadataResponse
from . import consts


class FilterService(BaseService):
    state: dict[str, dict]

    async def get_base_filters(self) -> MetadataResponse:
        return await self.client.get(
            consts.GET_FILTERS, params=consts.BASE_FILTER_PARAMS
        )

    async def get_filters(self, parent: int) -> MetadataResponse:
        return await self.client.get(
            consts.GET_FILTERS,
            params={"parent": parent, **consts.FILTERS_PARAMS},
        )

    async def load_filters(self):
        _filters = await self.get_base_filters()
        # There are should be something that saving to the state cities, categories and other
        # important things that respond from this method
