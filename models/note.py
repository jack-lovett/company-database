"""Note model for SQL database."""
from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime, func, String
from sqlalchemy.orm import relationship

from models import Base


class Note(Base):
    """Note model class"""
    __tablename__ = 'note'

    note_id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('project.project_id'))
    client_id = Column(Integer, ForeignKey('client.client_id'))
    note_type = Column(String(45), nullable=False)
    note_content = Column(Text, nullable=False)
    note_creation_datetime = Column(DateTime, nullable=False, default=func.current_timestamp())

    project = relationship("Project", backref="notes")
    client = relationship("Client", backref="notes")
