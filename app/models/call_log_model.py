from sqlalchemy import Integer, Column, ForeignKey, Enum, DateTime, func, String
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class CallLog(Base):
    __tablename__ = "call_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    staff_id = Column(Integer, ForeignKey('staff.id'), nullable=False)
    project_id = Column(Integer, ForeignKey('project.id'), nullable=True)
    type = Column(Enum('lead', 'information_request', name='type_enum'), nullable=False)
    status = Column(Enum('follow_up', 'resolved', 'in_progress', name='status_enum'), nullable=False)
    datetime = Column(DateTime, default=func.now(),
                      nullable=False)  # Automatically set to current timestamp
    description = Column(String(255), nullable=True)

    client = relationship("Client", back_populates="call_logs")
    staff = relationship("Staff", back_populates="call_logs")
    project = relationship("Project", back_populates="call_logs")
