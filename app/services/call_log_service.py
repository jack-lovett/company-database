from app.crud.call_log_crud import CRUDCall_log
from app.services.base_service import BaseService


class CallLogService(BaseService):
    def __init__(self):
        super().__init__(CRUDCall_log())
