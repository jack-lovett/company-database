"""Note model for SQL database."""
from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime, func, Enum
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class Note(Base):
    __tablename__ = "note"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('project.id'), nullable=True)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=True)
    type = Column(Enum('comment', 'reminder', 'follow_up', name='type_enum'), nullable=False)
    content = Column(Text, nullable=False)
    creation_datetime = Column(DateTime, default=func.now(), nullable=False)

    client = relationship("Client", back_populates="notes")
    project = relationship("Project", back_populates="notes")
