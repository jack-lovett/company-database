from app.crud.local_authority_crud import CRUDLocalAuthority
from app.services.base_service import BaseService


class LocalAuthorityService(BaseService):
    def __init__(self):
        super().__init__(CRUDLocalAuthority())
