"""Project model for SQL database."""
from sqlalchemy import Column, Integer, ForeignKey, Enum, Text, Date, DateTime, func
from sqlalchemy.orm import relationship

from models import Base


class Project(Base):
    """Project model class"""
    __tablename__ = 'project'

    project_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('client.client_id'), nullable=False)
    address_id = Column(Integer, ForeignKey('address.address_id'), nullable=False)
    project_status = Column(Enum('lead', 'job', 'completed', 'no_sale'), nullable=False)
    project_description = Column(Text, nullable=True)
    project_initial_inquiry_date = Column(Date, nullable=True)
    project_start_date = Column(Date, nullable=True)
    project_end_date = Column(Date, nullable=True)
    project_storeys = Column(Integer, nullable=True)
    project_referral_source = Column(
        Enum('google', 'referral', 'repeat_client', 'jkc', 'smce', 'word_of_mouth', 'website'), nullable=True)
    project_payment_basis = Column(Enum('lump_sum', 'hourly_rate'), nullable=True)
    project_creation_datetime = Column(DateTime, server_default=func.current_timestamp(), nullable=False)



    def __repr__(self):
        return f"<Project(id={self.project_id}, status={self.project_status})>"
