from sqlalchemy import Column, Integer, ForeignKey

from app.models.base_model import Base


class SiteOverlay(Base):
    __tablename__ = "site_overlay"

    overlay_id = Column(Integer, ForeignKey('overlay.id'), primary_key=True)
    site_id = Column(Integer, ForeignKey('site.id'), primary_key=True)
