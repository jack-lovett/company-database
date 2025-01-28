from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship

from models import Base


class Budget(Base):
    __tablename__ = "budget"

    budget_id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('project.project_id'), nullable=False)
    budget_type = Column(Enum('asset', 'liability', name='budget_type_enum'), nullable=False)
    budget_status = Column(Enum('not_invoiced', 'invoiced', 'paid', 'partially_invoiced', name='budget_status_enum'),
                           default='not_invoiced',
                           nullable=False)
    budget_description = Column(String(255), nullable=True)
    budget_estimate = Column(DECIMAL(10, 2), nullable=True)
    budget_actual = Column(DECIMAL(10, 2), nullable=True)

    project = relationship("Project", back_populates="budgets")
