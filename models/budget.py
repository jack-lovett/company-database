"""Budget model for SQL database."""
from sqlalchemy import Integer, Column, ForeignKey, Enum, String
from sqlalchemy.orm import relationship

from models import Base


class Budget(Base):
    """Budget model class"""
    __tablename__ = 'budget'

    budget_id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('project.project_id'), nullable=False)
    budget_type = Column(Enum('asset', 'liability'), nullable=False)
    budget_status = Column(Enum('not_invoiced', 'invoiced', 'paid'), nullable=False, default='not_invoiced')
    budget_description = Column(String(45))
    budget_estimate = Column(String(45))
    budget_actual = Column(String(45))

    project = relationship("Project", backref="budgets")
