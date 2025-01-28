"""Note model for SQL database."""
from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime, func, Enum
from sqlalchemy.orm import relationship

from models import Base


class Note(Base):
    __tablename__ = "note"

    note_id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('project.project_id'), nullable=True)
    client_id = Column(Integer, ForeignKey('client.client_id'), nullable=True)
    note_type = Column(Enum('comment', 'reminder', 'follow_up', name='note_type_enum'), nullable=False)
    note_content = Column(Text, nullable=False)
    note_creation_datetime = Column(DateTime, default=func.now(), nullable=False)

    client = relationship("Client", back_populates="notes")
    project = relationship("Project", back_populates="notes")
