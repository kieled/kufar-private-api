from base import BaseService
from packages.account.schemas import GetCurrentAccountResponse
from utils.auth import auth_required

from . import consts


class AccountService(BaseService):
    @auth_required
    async def get_current_account(self) -> GetCurrentAccountResponse:
        return await self.client.get(consts.GET_CURRENT_ACCOUNT)
