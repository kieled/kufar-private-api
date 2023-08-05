from . import consts
from .schemas import (
    GetCategoriesResponse
)

from base import BaseService


class CategoryService(BaseService):
    async def get_categories(self) -> GetCategoriesResponse:
        return await self.client.get(consts.GET_CATEGORIES)
