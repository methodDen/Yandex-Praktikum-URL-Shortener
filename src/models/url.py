from sqlalchemy import (
    Column,
    String, Integer,
)
from sqlalchemy.orm import relationship

from src.db.base_class import Base
from src.models.mixins import TimestampMixin


class Url(
    TimestampMixin,
    Base,
):
    __tablename__ = "url"
    original_url = Column(String(1024), nullable=False,)
    short_url = Column(String(1024), nullable=False, unique=True)
    number_of_visits = Column(Integer, default=0)
    visits = relationship("Visit", back_populates="url", order_by="Visit.id")

    def __repr__(self):
        return (
            "<Url(original_url='%s')>"
            % (
                self.original_url,
            )
        )
