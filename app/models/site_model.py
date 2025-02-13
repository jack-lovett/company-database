from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class Site(Base):
    __tablename__ = "site"

    id = Column(Integer, primary_key=True, autoincrement=True)
    address_id = Column(Integer, ForeignKey('address.id'), nullable=False)
    local_authority_id = Column(Integer, ForeignKey('local_authority.id'), nullable=False)
    wind_class_id = Column(Integer, ForeignKey('wind_class.id'), nullable=False)
    soil_class_id = Column(Integer, ForeignKey('soil_class.id'), nullable=False)
    lot_number = Column(Integer, nullable=True)
    plan_number = Column(String(15), nullable=True)
    heritage_status = Column(Boolean, nullable=True)
    zone = Column(String(45), nullable=True)
    precinct = Column(String(45), nullable=True)
    area = Column(String(45), nullable=True)

    address = relationship("Address", back_populates="sites")
    local_authority = relationship("LocalAuthority", back_populates="sites")
    wind_class = relationship("WindClass", back_populates="sites")
    soil_class = relationship("SoilClass", back_populates="sites")
    overlays = relationship("Overlay", secondary="site_overlay", back_populates="sites")
    projects = relationship("Project", back_populates="site")
