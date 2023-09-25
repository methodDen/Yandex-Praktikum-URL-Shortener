from pydantic import BaseModel, Field, HttpUrl


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