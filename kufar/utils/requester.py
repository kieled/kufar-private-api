from json import JSONDecodeError
from typing import Literal, Self

from aiohttp import ClientSession, ContentTypeError

from .signature_decoder import decode_signature
from ..base import consts


class Requester:
    __base_url: str
    __client: ClientSession | None = None
    __headers: dict[str, str]
    __hash: str = ""

    def __init__(self):
        self.__base_url = ""
        self.__headers = consts.BASE_HEADERS

    async def __aenter__(self) -> Self:
        self.__client = ClientSession(
            base_url=self.__base_url if len(self.__base_url) else None,
            headers=self.__headers,
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.__client:
            await self.__client.close()
        self.__client = None

    @property
    def url(self):
        return self.__base_url

    @url.setter
    def url(self, value: str):
        self.__base_url = value

    async def post(self, path: str, payload: dict | None = None, **kwargs):
        prev_headers = kwargs.get("headers") or {}
        kwargs.update(
            {
                "headers": {
                    **prev_headers,
                    "content-type": "application/json; charset=UTF-8",
                }
            }
        )
        return await self._request("POST", path, json=payload, **kwargs)

    async def get(self, path: str, **kwargs):
        return await self._request("GET", path, **kwargs)

    async def delete(self, path: str, **kwargs):
        return await self._request("DELETE", path, **kwargs)

    async def post_legacy(self, path: str, **kwargs):
        return await self._legacy_request("POST", path, **kwargs)

    async def get_legacy(self, path: str, **kwargs):
        return await self._legacy_request("GET", path, **kwargs)

    @property
    def headers(self):
        return self.__headers

    def patch_headers(self, new_headers: dict[str, str]):
        self.__headers = {**self.__headers, **new_headers}
        if self.__client:
            self.__client.headers.update(self.__headers)

    def select_headers(self, *args: str):
        if len(args) == 1:
            return self.__headers.get(args[0])
        return {k: v for k, v in self.__headers.items() if k in args}

    async def _request(
        self, method: Literal["GET", "POST", "PUT", "DELETE"], path: str, **kwargs
    ):
        if not self.__client:
            raise Exception(
                "Not initialized client. You should use async context manager"
            )
        if not self.__base_url:
            raise Exception("base_url not specified")
        if kwargs.get("headers"):
            kwargs["headers"] = {
                **self.__headers,
                **kwargs.get("headers"),  # type: ignore
            }
        else:
            kwargs["headers"] = self.__headers
        url = f"{self.__base_url}{path}"
        params = exclude_none(kwargs.get("params") or {})
        kwargs.pop("params")
        async with self.__client.request(method, url, **kwargs, params=params) as res:
            try:
                return await res.json()
            except (ContentTypeError, JSONDecodeError) as e:
                print(f"Error while decoding. Content: {await res.text()}")
                raise e

    async def _legacy_request(self, method: str, path: str, **kwargs) -> any:  # type: ignore
        url = f"{self.__base_url}{path}"
        if not self.__client:
            return None
        headers: dict = (
            self.select_headers(
                "user-agent", "x-app-name", "x-app-version", "x-device-id"
            )
            or {}
        )  # type: ignore
        async with self.__client.request(
            method,
            url,
            **kwargs,
            allow_redirects=False,
            params={
                "app_id": "android",
                "account_token": self.select_headers("session-id"),
                "hash": decode_signature(self.__hash),
                **(exclude_none(kwargs.get("params") or {})),
            },
            headers={**headers, **(kwargs.get("headers") or {})},
        ) as res:
            try:
                data = await res.json()
            except (ContentTypeError, JSONDecodeError) as e:
                print(f"Error while decoding. Content: {(await res.text())[:1000]}")
                raise e
        if "authorize" in data:
            self.__hash = str(data.get("authorize").get("challenge", ""))
            return await self._legacy_request(method, path)
        return data


def exclude_none(input: dict) -> dict:
    return {k: v for k, v in input.items() if v is not None}
