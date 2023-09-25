from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl
from src.schemas.visit import VisitNestedSchema


class UrlBaseSchema(BaseModel):
    url: str


class UrlCreateSchema(UrlBaseSchema):
    pass


class UrlUpdateSchema(UrlBaseSchema):
    pass


class UrlResponseSchema(UrlBaseSchema):
    url: str = Field(..., alias='original_url')
    short_url: str


class UrlRequestCreateSchema(BaseModel):
    url: HttpUrl = Field(..., alias='original_url')


class UrlStatsResponseSchema(BaseModel):
    url: str = Field(..., alias='original_url')
    short_url: str
    visits_count: int


class UrlFullStatsResponseSchema(UrlStatsResponseSchema):
    visits: Optional[List[VisitNestedSchema]] = None
