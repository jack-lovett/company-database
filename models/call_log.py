from sqlalchemy import Integer, Column, ForeignKey, Enum, DateTime, Text, func
from sqlalchemy.orm import relationship

from models import Base


class CallLog(Base):
    __tablename__ = "call_log"

    call_log_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('client.client_id'), nullable=False)
    staff_id = Column(Integer, ForeignKey('staff.staff_id'), nullable=False)
    project_id = Column(Integer, ForeignKey('project.project_id'), nullable=True)
    call_log_type = Column(Enum('lead', 'information_request', name='call_log_type_enum'), nullable=False)
    call_log_status = Column(Enum('follow_up', 'resolved', name='call_log_status_enum'), nullable=False)
    call_log_datetime = Column(DateTime, server_default="CURRENT_TIMESTAMP",
                               nullable=False)  # Automatically set to current timestamp
    call_log_description = Column(Text, nullable=True)

    client = relationship("Client", back_populates="call_logs")
    staff = relationship("Staff", back_populates="call_logs")
    project = relationship("Project", back_populates="call_logs")
