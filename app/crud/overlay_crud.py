from app.crud.base_crud import CRUDBase
from app.models.overlay_model import Overlay


class CRUDOverlay(CRUDBase):
    def __init__(self):
        super().__init__(Overlay)
