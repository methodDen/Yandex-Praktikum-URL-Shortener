from src.crud.base import CRUDBase
from src.models import Url
from src.schemas.url import (
    UrlCreateSchema,
    UrlUpdateSchema,
)


class CRUDUrl(CRUDBase[Url, UrlCreateSchema, UrlUpdateSchema]):
    pass


url = CRUDUrl(Url)