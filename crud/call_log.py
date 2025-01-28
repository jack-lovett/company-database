from crud.base import CRUDBase
from models.call_log import CallLog

class CRUDCall_log(CRUDBase):
    def __init__(self):
        super().__init__(CallLog)