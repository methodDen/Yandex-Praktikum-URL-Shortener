from sqlalchemy import (
    Column,
    String,
    Integer,
    TIMESTAMP,
    func,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from src.db.base_class import Base
from src.models.mixins import TimestampMixin


class Visit(
    TimestampMixin,
    Base,
):
    __tablename__ = "visit"
    user_ip = Column(String(1024), nullable=False,)
    visit_datetime = Column(TIMESTAMP(), nullable=False, default=func.now())
    url_id = Column(Integer, ForeignKey("url.id"))
    url = relationship("Url", back_populates="visits")

    def __repr__(self):
        return (
            "<Visit(user_ip='%s')>"
            % (
                self.user_ip,
            )
        )
