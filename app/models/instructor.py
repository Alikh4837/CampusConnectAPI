from sqlmodel import SQLModel, Field,Relationship
from typing import Optional,List,TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.department import Department
    from app.models.section import Section


class InstructorBase(SQLModel):
    name: str
    phone: str
    address: str
    password:str
    emergency_contact: Optional[str]


class Instructor(InstructorBase):
    id: int = Field(primary_key=True)

    departments:List["Department"]=Relationship(back_populates="instructors")
    sections:List["Section"]=Relationship(back_populates="sections")