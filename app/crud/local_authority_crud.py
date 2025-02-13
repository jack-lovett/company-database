from app.crud.base_crud import CRUDBase
from app.models.local_authority_model import LocalAuthority


class CRUDLocalAuthority(CRUDBase):
    def __init__(self):
        super().__init__(LocalAuthority)
