from sqlalchemy import (
    Column,
    String,
)

from src.db.base_class import Base
from src.models.mixins import TimestampMixin


class Url(
    TimestampMixin,
    Base,
):
    __tablename__ = "url"
    original_url = Column(String(1024), unique=True)

    def __repr__(self):
        return (
            "<Url(original_url='%s')>"
            % (
                self.original_url,
            )
        )
