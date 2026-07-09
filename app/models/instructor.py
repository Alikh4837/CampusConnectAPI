from sqlmodel import SQLModel, Field,Relationship
from typing import Optional,List,TYPE_CHECKING
from app.models.department import Department
from app.models.Section import Section

if TYPE_CHECKING:
    from app.models.department import Department
    from app.models.Section import Section


class InstructorBase(SQLModel):
    name: str
    phone: int
    address: str
    password:str
    emergency_contact: Optional[int]


class Instructor(InstructorBase):
    id: int = Field(primary_key=True)

    departments:List["Department"]=Relationship(back_populates="Instructor")
    sections:List["Section"]=Relationship(back_populates="Instructor")