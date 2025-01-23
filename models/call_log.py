"""Call log model for SQL database."""
from sqlalchemy import Integer, Column, ForeignKey, Enum, DateTime, Text, func
from sqlalchemy.orm import relationship

from models import Base


class CallLog(Base):
    """Call log model class"""

    __tablename__ = 'call_log'
    call_log_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('client.client_id'), nullable=False)
    staff_id = Column(Integer, ForeignKey('staff.staff_id'), nullable=False)
    project_id = Column(Integer, ForeignKey('project.project_id'))
    call_log_type = Column(Enum('lead', 'information_request'), nullable=False)
    call_log_status = Column(Enum('follow_up', 'resolved'), nullable=False)
    call_log_datetime = Column(DateTime, default=func.current_timestamp())
    call_log_description = Column(Text)

    client = relationship("Client", backref="call_logs")
    staff = relationship("Staff", backref="call_logs")
    project = relationship("Project", backref="call_logs")
