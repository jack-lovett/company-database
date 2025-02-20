from app.crud.overlay_crud import CRUDOverlay
from app.services.base_service import BaseService


class SiteOverlayService(BaseService):
    def __init__(self):
        super().__init__(CRUDOverlay())
