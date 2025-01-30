from crud.call_log import CRUDCall_log
from services.base import BaseService


class CallLogService(BaseService):
    def __init__(self):
        super().__init__(CRUDCall_log())
