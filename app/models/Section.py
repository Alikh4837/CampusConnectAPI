from sqlmodel import SQLModel, Field,Relationship
from typing import Optional,List,TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.course import Course
    from app.models.term import Term
    from app.models.room import Room
    from app.models.instructor import Instructor
    from app.models.enrollment import Enrollment



class SectionBase(SQLModel):
    section_name:str

class Section(SectionBase,table=True):
    id:int=Field(primary_key=True)

    course_id:Optional[int]=Field(default=None,foreign_key="course.id")
    term_id:Optional[int]=Field(default=None,foreign_key="term.id")
    room_id:Optional[int]=Field(default=None,foreign_key="room.id")
    instructor_id:Optional[int]=Field(default=None,foreign_key="instructor.id")

    course:Optional["Course"]=Relationship(back_populates="sections")
    term:Optional["Term"]=Relationship(back_populates="sections")
    room:Optional["Room"]=Relationship(back_populates="sections")
    instructor:Optional["Instructor"]=Relationship(back_populates="sections")
    enrollments:List["Enrollment"]=Relationship(back_populates="sections")