from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class WindClass(Base):
    __tablename__ = "wind_class"

    id = Column(Integer, primary_key=True, autoincrement=True)
    class_ = Column('class', String(2), nullable=True)

    sites = relationship("Site", back_populates="wind_class")
