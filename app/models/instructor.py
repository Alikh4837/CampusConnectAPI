from sqlmodel import SQLModel, Field,Relationship
from typing import Optional,List,TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.department import Department
    from app.models.section import Section


class InstructorBase(SQLModel):
    name: str
    phone: str
    email:str
    address: str
    password:str
    emergency_contact: Optional[str]=None


class Instructor(InstructorBase,table=True):
    id: int = Field(primary_key=True)

    department_id:Optional[int]=Field(default=None,foreign_key="department.id")

    department:Optional["Department"]=Relationship(back_populates="instructors")
    sections:List["Section"]=Relationship(back_populates="instructor")