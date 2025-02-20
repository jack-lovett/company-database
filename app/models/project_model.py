from datetime import date, datetime
from enum import Enum
from typing import Optional, List

from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field, Relationship

from app.models.project_is_building_class_model import ProjectIsBuildingClass
from app.models.staff_project_model import StaffProject
from app.models.project_has_contractor_model import ProjectHasContractor


class ProjectStatus(str, Enum):
    lead = "lead"
    job = "job"
    completed = "completed"
    no_sale = "no_sale"


class ReferralSource(str, Enum):
    google = "google"
    referral = "referral"
    repeat_client = "repeat_client"
    jkc = "jkc"
    smce = "smce"
    word_of_mouth = "word_of_mouth"
    website = "website"


class PaymentBasis(str, Enum):
    lump_sum = "lump_sum"
    hourly_rate = "hourly_rate"


class ProjectBase(SQLModel):
    number: int = Field(unique=True)
    client_id: int = Field(foreign_key="client.id")
    site_id: int = Field(foreign_key="site.id")
    status: ProjectStatus
    description: Optional[str] = Field(default=None)
    initial_inquiry_date: date
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    storeys: Optional[int] = None
    referral_source: Optional[ReferralSource] = None
    payment_basis: Optional[PaymentBasis] = None
    creation_datetime: datetime = Field(default_factory=datetime.utcnow)


class Project(ProjectBase, table=True):
    __tablename__ = "project"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationships
    contractors: List["Contractor"] = Relationship(
        back_populates="projects",
        link_model=ProjectHasContractor
    )
    budgets: List["Budget"] = Relationship(back_populates="project")
    client: "Client" = Relationship(back_populates="projects")
    building_classes: List["BuildingClass"] = Relationship(
        back_populates="projects",
        link_model=ProjectIsBuildingClass
    )
    staff: List["Staff"] = Relationship(
        back_populates="projects",
        link_model=StaffProject
    )
    staff_times: List["StaffTime"] = Relationship(back_populates="project")
    notes: List["Note"] = Relationship(back_populates="project")
    site: "Site" = Relationship(back_populates="projects")
    call_logs: List["CallLog"] = Relationship(back_populates="project")


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(SQLModel):
    status: Optional[ProjectStatus] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    storeys: Optional[int] = None
    referral_source: Optional[ReferralSource] = None
    payment_basis: Optional[PaymentBasis] = None


class ProjectDisplay(SQLModel):
    id: int
    number: int
    client_name: str
    site: str
    status: ProjectStatus
    description: Optional[str] = None
    initial_inquiry_date: date
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    storeys: Optional[int] = None
    referral_source: Optional[ReferralSource] = None
    payment_basis: Optional[PaymentBasis] = None
    creation_datetime: datetime
