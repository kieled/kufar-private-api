from base import BaseService
from . import consts
from .schemas import (
    SavedSearch,
    SavedSearches
)


class SavedService(BaseService):
    async def mark_search_seen(self, account_id: int, search_id: int) -> None:
        return await self.client.post(consts.MARK_SEARCH_SEEN.format(
            account_id=account_id,
            search_id=search_id
        ))

    async def delete_search(self, account_id: int, search_id: int) -> None:
        return await self.client.delete(consts.DELETE_SEARCH.format(
            account_id=account_id,
            search_id=search_id
        ))

    async def get_searches(self, account_id: int, cursor: str | None = None) -> SavedSearches:
        return await self.client.get(consts.GET_FAVORITE_SEARCHES.format(
            account_id=account_id
        ), params={
            'cursor': cursor
        })

    async def save_search(self, account_id: int, query: str) -> SavedSearch:
        return await self.client.post(consts.SAVE_SEARCH.format(
            account_id=account_id
        ), {
            'query': query
        })
