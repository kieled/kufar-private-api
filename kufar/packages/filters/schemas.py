from typing import Literal

from pydantic import BaseModel


class ParamsRefValue(BaseModel):
    value: str
    labels: dict[Literal["ru", "by"], str]
    hint: str | None = None
    image_url: str | None = None


class ParamsRefUIComponent(BaseModel):
    fallback_type: str | None = None
    type: str | None = None


class LanguageRef(BaseModel):
    ru: str
    by: str


class RangeRef(BaseModel):
    default_lower: int
    default_upper: int
    lower: int
    step: int
    upper: int


class ParamsRef(BaseModel):
    variation_id: int
    name: str
    url_name: str
    required: bool
    type: str
    meta: str
    multi: bool
    ui_component: ParamsRefUIComponent | None = None
    # actions: any
    labels: dict[str, dict[Literal["by", "ru"], str]]
    values: list[ParamsRefValue] | None = None
    external_values_url: str | None = None
    range: RangeRef | None = None
    min_taxonomy_version: int
    hint: LanguageRef | None = None
    image_url: str | None = None
    is_type: bool


class ParamsRule(BaseModel):
    rule: dict[str, str]
    refs: list[str]


class ParametersOrder(BaseModel):
    dispatch_type: Literal["many", "one"]
    deduplication_key: Literal["name"] | None = None
    refs: dict[str, ParamsRef]
    rules: list[ParamsRule]


class ParamsMetadata(BaseModel):
    parameters: ParametersOrder


class MetadataResponse(BaseModel):
    metadata: ParamsMetadata
