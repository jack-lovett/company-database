from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class Overlay(Base):
    __tablename__ = "overlay"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=True)

    sites = relationship("Site", secondary="site_overlay", back_populates="overlays")

    def __str__(self):
        return self.name
