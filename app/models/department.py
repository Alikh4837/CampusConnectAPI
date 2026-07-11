from sqlmodel import SQLModel,Field,Relationship
from typing import List,TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.instructor import Instructor
    from app.models.course import Course


class DepartmentBase(SQLModel):
    dept_name:str
    dept_code:int

class Department(DepartmentBase):
    id:int=Field(primary_key=True)

    instructors:List["Instructor"]=Relationship(back_populates="departments")
    Courses:List["Course"]=Relationship(back_populates="courses")