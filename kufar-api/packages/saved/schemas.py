from pydantic import BaseModel

__all__ = [
    'SavedSearch',
    'Counters',
    'AutoNames',
    'SavedSearches'
]


class AutoNames(BaseModel):
    by: str
    ru: str


class Counters(BaseModel):
    new: int | None = None
    total: int | None = None


class SavedSearch(BaseModel):
    auto_names: AutoNames | None = None
    query: str | None = None
    counters: Counters | None = None
    created_at: int | None = None


class SavedSearches(BaseModel):
    items: list[SavedSearch]
    cursor: str | None = None
