from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession

from src.crud.base import CRUDBase
from src.models import Url
from src.schemas.url import (
    UrlCreateSchema,
    UrlUpdateSchema,
)
from src.services.url import generate_random_url


class CRUDUrl(CRUDBase[Url, UrlCreateSchema, UrlUpdateSchema]):
    async def create(self, db: AsyncSession, *, obj_in: UrlCreateSchema) -> Url:
        """
        Create a new row in the database
        """
        obj_in_data = jsonable_encoder(obj_in)
        obj_in_data['short_url'] = generate_random_url()
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def create_multi(self, db: AsyncSession, *, obj_in: UrlCreateSchema) -> List[Url]:
        """
        Create multiple rows in the database
        """
        obj_in_data = jsonable_encoder(obj_in)
        obj_in_data = [dict(obj, short_url=generate_random_url()) for obj in obj_in_data]
        db_objs = [self.model(**obj_in_data) for obj_in_data in obj_in_data]
        db.add_all(db_objs)
        await db.commit()
        for db_obj in db_objs:
            await db.refresh(db_obj)
        return db_objs


url = CRUDUrl(Url)