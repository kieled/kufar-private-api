from typing import Literal

from pydantic import BaseModel


class CityListRefValue(BaseModel):
    value: str
    labels: dict[Literal['ru', 'by'], str]
    hint: str | None = None
    image_url: str | None = None


class CityListRefUIComponent(BaseModel):
    fallback_type: str
    type: str


class CityListRef(BaseModel):
    variation_id: int
    name: str
    url_name: str
    required: bool
    type: str
    meta: str
    multi: bool
    ui_component: CityListRefUIComponent
    # actions: any
    labels: dict[str, dict[Literal['by', 'ru'], str]]
    values: list[CityListRefValue]
    external_values_url: str | None = None
    # range: any
    min_taxonomy_version: int
    hint: str | None = None
    image_url: str | None = None
    is_type: bool


class CityListRule(BaseModel):
    rule: dict[str, str]
    refs: list[str]


class CityListParameters(BaseModel):
    dispatch_type: Literal['many']
    deduplication_key: Literal['name']
    refs: dict[str, CityListRef]
    rules: list[CityListRule]


class CityListMetadata(BaseModel):
    parameters: CityListParameters
    # parameters_order: any


class CityListResponse(BaseModel):
    metadata: CityListMetadata
