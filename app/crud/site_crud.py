from app.crud.base_crud import CRUDBase
from app.models.site_model import Site


class CRUDSite(CRUDBase):
    def __init__(self):
        super().__init__(Site)
