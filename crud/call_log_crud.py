from crud.base_crud import CRUDBase
from models.call_log_model import CallLog


class CRUDCall_log(CRUDBase):
    def __init__(self):
        super().__init__(CallLog)
