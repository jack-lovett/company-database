from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.overlay_schema import Overlay, OverlayCreate
from app.services.overlay_service import OverlayService

router = APIRouter(prefix="/overlays", tags=["overlays"])


@router.post("/", response_model=Overlay)
def create_overlay(overlay: OverlayCreate, database: Session = Depends(get_database)):
    service = OverlayService()
    return service.create(database, overlay.dict())


@router.get("/", response_model=list[Overlay])
def get_overlays(database: Session = Depends(get_database)):
    service = OverlayService()
    return service.get_all(database)
