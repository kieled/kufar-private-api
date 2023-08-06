import inspect
from dataclasses import dataclass
from functools import wraps

from pydantic import BaseModel, ValidationError
from kufar.utils.requester import Requester


@dataclass
class BaseService:
    client: Requester
    base_url: str

    def __getattribute__(self, item: str):
        attr = super().__getattribute__(item)

        if callable(attr):
            return_type = inspect.signature(attr).return_annotation

            if not return_type:
                return attr

            if inspect.isclass(return_type) and issubclass(return_type, BaseModel):

                @wraps(attr)
                async def wrapper_func(*args, **kwargs):
                    self.client.url = self.base_url
                    response = await attr(*args, **kwargs)
                    try:
                        return return_type.model_validate(response)
                    except ValidationError as e:
                        print(
                            f"Error while validating response. Response is: {response}\nError is: {e}"
                        )
                        return None

                return wrapper_func
        return attr
