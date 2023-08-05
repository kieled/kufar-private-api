from pydantic import BaseModel

__all__ = [
    'Category',
    'GetCategoriesResponse',
    'Subcategory'
]


class Subcategory(BaseModel):
    id: str
    parent: str
    order: str
    name: str
    name_ru: str
    name_by: str


class Category(BaseModel):
    id: str
    name: str
    name_ru: str
    name_by: str
    version: str
    order: str
    subcategories: list


class GetCategoriesResponse(BaseModel):
    categories: list[Category]
