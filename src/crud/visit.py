from src.crud.base import CRUDBase
from src.models import Visit
from src.schemas.visit import (
    VisitCreateSchema,
    VisitUpdateSchema,
)


class CRUDVisit(CRUDBase[Visit, VisitCreateSchema, VisitUpdateSchema]):
    pass


visit = CRUDVisit(Visit)