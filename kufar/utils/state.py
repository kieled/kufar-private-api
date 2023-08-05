import json
import os

import aiofiles


class State:
    __state: dict[str, str | int]
    __file_path: str

    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.__state = {}

    async def load(self) -> None:
        if os.path.isfile(self.__file_path):
            async with aiofiles.open(self.__file_path, 'r') as f:
                self.__state = json.loads(await f.read())
        
    async def save(self) -> None:
        async with aiofiles.open(self.__file_path, 'w') as f:
            await f.write(json.dumps(self.__state))

    def __getattr__(self, name: str) -> str | int | None:
        return object.__getattribute__(self, '_State__state').get(name, None)
    
    def __setattr__(self, name: str, value: str | int) -> None:
        if name in self.__annotations__.keys():
            return object.__setattr__(self, name, value)
        object.__getattribute__(self, '_State__state')[name] = value
