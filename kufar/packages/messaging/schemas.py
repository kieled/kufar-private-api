from pydantic import BaseModel

__all__ = ['UnreadMessagesCountResponse']

class UnreadMessagesCountResponse(BaseModel):
    unread: int