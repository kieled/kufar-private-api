from datetime import datetime
from enum import Enum

from pydantic import BaseModel

__all__ = [
    'MyAd',
    'ModifyAdResponse',
    'Thumb',
    'MyAdStatistics',
    'MyAdsCounterResponse',
    'AdStatusEnum',
    'MyAdsCounter',
    'MyAdsResponse',
]


class ModifyAdResponse(BaseModel):
    status: str
    success_header: str
    success_description: str
    success_ok_button: str
    error_header: str
    error_description: str
    error_ok_button: str
    error_buy_button: str
    error_label: str


class MyAdsCounter(BaseModel):
    status: str
    value: int


class MyAdsCounterResponse(BaseModel):
    counters: list[MyAdsCounter]
    status: str


class AdStatusEnum(Enum):
    PENDING_REVIEW = 'PENDING_REVIEW'
    DEACTIVATED = 'DEACTIVATED'
    INACTIVE = 'INACTIVE'
    PENDING_SLOT = 'PENDING_SLOT'
    REFUSED = 'REFUSED'
    ACTIVE = 'ACTIVE'
    PENDING_REVIEW_AFTER_EDIT = 'PENDING_REVIEW_AFTER_EDIT'
    PENDING_REVIEW_AFTER_ACTIVATION = 'PENDING_REVIEW_AFTER_ACTIVATION'
    DELETED = 'DELETED'
    HIDDEN = 'HIDDEN'


class MyAdStatistics(BaseModel):
    view: int
    phone: int
    favorite: int


class Thumb(BaseModel):
    image_id: str
    media_storage: str
    path: str
    yams_storage: bool


class MyAd(BaseModel):
    ad_id: int
    list_id: int | None = None
    action_id: int
    ad_status: AdStatusEnum
    db_status: AdStatusEnum
    body: str | None = None
    category: int
    category_name: str
    category_parent: int
    category_parent_name: str
    company_ad: bool
    currency: str
    date: datetime | None = None
    date_expired: datetime | None = None
    delete_from_date: datetime | None = None
    highlight: bool
    phone_hidden: bool
    polepos: bool
    safedeal_enabled: bool
    price: int | None = None
    price_suffix: str | None = None
    prolong_perm: bool
    ribbons: str | None = None
    subject: str | None = None
    remuneration_type: str | None = None
    thumbs: list[Thumb]
    statistics: MyAdStatistics | None = None
    delivery_enabled: bool
    halva: bool
    delete_perm: bool
    region: int
    region_name: str | None = None
    activate_perm: bool
    is_favourite: bool
    link: str | None = None
    polepos_end: datetime | None = None
    highlight_end: datetime | None = None
    ribbons_end: datetime | None = None


class MyAdsResponse(BaseModel):
    status: str
    total: int
    numperpage: int
    ads: list[MyAd]
