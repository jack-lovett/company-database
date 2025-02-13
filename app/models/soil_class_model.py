from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class SoilClass(Base):
    __tablename__ = "soil_class"

    id = Column(Integer, primary_key=True, autoincrement=True)
    abbreviation = Column(String(45), nullable=False)
    class_ = Column('class', String(45), nullable=False)
    description = Column(String(45), nullable=False)

    sites = relationship("Site", back_populates="soil_class")
