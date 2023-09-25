from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import load_only

from src.crud.base import CRUDBase
from src.models import Visit
from src.schemas.visit import (
    VisitCreateSchema,
    VisitUpdateSchema,
)


class CRUDVisit(CRUDBase[Visit, VisitCreateSchema, VisitUpdateSchema]):

    async def get_visits_by_url_id(
        self,
        db: AsyncSession,
        url_id: int,
        skip: int = 0,
        limit: int = 0,
    ) -> List[Visit]:
        """
        Get multiple ORM-level SQL construction object
        """
        query = (select(
            self.model
        ).where(
            self.model.url_id == url_id
        ).options(load_only(
            self.model.user_ip,
            self.model.visit_datetime,
        )
        ).offset(skip).limit(limit))
        result = await db.execute(query)
        return result.scalars().all()


visit = CRUDVisit(Visit)
