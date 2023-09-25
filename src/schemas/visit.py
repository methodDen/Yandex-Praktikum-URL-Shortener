import datetime

from pydantic import BaseModel


class VisitBaseSchema(BaseModel):
    user_ip: str
    visit_datetime: datetime.datetime
    url_id: int


class VisitCreateSchema(VisitBaseSchema):
    pass


class VisitUpdateSchema(VisitBaseSchema):
    pass