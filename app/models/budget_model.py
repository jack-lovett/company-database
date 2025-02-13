from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship

from app.models.base_model import Base


class Budget(Base):
    __tablename__ = "budget"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('project.id'), nullable=False)
    type = Column(Enum('asset', 'liability', name='type_enum'), nullable=False)
    status = Column(Enum('not_invoiced', 'invoiced', 'paid', 'partially_invoiced', name='status_enum'),
                    default='not_invoiced',
                    nullable=False)
    description = Column(String(255), nullable=True)
    estimate = Column(DECIMAL(10, 2), nullable=True)
    actual = Column(DECIMAL(10, 2), nullable=True)

    project = relationship("Project", back_populates="budgets")
