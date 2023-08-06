from kufar.base.service import BaseService
from kufar.utils.auth import auth_required

from . import consts
from .schemas import UnreadMessagesCountResponse


class MessagingService(BaseService):
    @auth_required
    async def unread_count(self) -> UnreadMessagesCountResponse:
        return await self.client.get(consts.MESSAGES_COUNTER)
