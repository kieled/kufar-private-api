from pydantic import BaseModel
from typing import Literal

__all__ = [
    'Advert',
    'Image',
    'Page',
    'Pagination',
    'GetAdvertResponse',
    'Parameter',
    'GetPhoneResponse',
    'PaidService',
    'GetAdvertByListIdResponse',
    'GetUserSearchAdvertsResponse'
]


class Image(BaseModel):
    id: str
    media_storage: str
    path: str
    yams_storage: bool


class PaidService(BaseModel):
    highlight: bool
    polepos: bool
    ribbons: str
    halva: bool


class Parameter(BaseModel):
    name_label: str
    value_label: str
    name: str
    value: str


class Advert(BaseModel):
    ad_id: int
    account_id: int
    images: list[Image]
    account_parameters: list[Parameter]
    ad_parameters: list[Parameter]
    list_time: int | None = None
    paid_services: list[PaidService] | None = None
    list_id: int | None = None
    message_id: str | None = None
    price_usd: int | None = None
    price_eur: int | None = None
    price_byn: int | None = None
    remuneration_type: str | None = None
    company_ad: bool | None = None
    phone: str | None = None
    category: str | None = None
    subject: str | None = None
    body: str | None = None
    type: str | None = None
    ad_link: str | None = None
    phone_hidden: bool | None = None
    currency: Literal['BYN', 'USD'] | None = None


class GetAdvertResponse(BaseModel):
    result: Advert


class GetAdvertByListIdResponse(BaseModel):
    ads: list[Advert]


class GetPhoneResponse(BaseModel):
    phone: str


class Page(BaseModel):
    label: Literal['next', 'prev']
    num: int
    token: str


class Pagination(BaseModel):
    pages: list[Page]


class GetUserSearchAdvertsResponse(BaseModel):
    total: int
    ads: list[Advert]
    pagination: Pagination
