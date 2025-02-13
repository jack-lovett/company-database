from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class LocalAuthority(Base):
    __tablename__ = "local_authority"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    website = Column(String(45), nullable=True)

    sites = relationship("Site", back_populates="local_authority")
