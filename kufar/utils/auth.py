from functools import wraps
from typing import Callable, TypeVar

F = TypeVar('F', bound=Callable)


class UnauthorizedException(Exception):
    def __init__(self):
        super().__init__('method required authorization. You can use method `authenticate`')


def auth_required(f: F) -> F:
    @wraps(f)
    async def wrapper(*args, **kwargs):
        instance = args[0]
        session_id = instance.client.headers.get('session-id')
        token = instance.client.headers.get('authorization')
        if not session_id or not token:
            raise UnauthorizedException()
        return await f(*args, **kwargs)

    return wrapper # type: ignore
