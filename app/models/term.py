from sqlmodel import SQLModel, Field,Relationship
from typing import Optional,List,TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.section import Section


class TermBase(SQLModel):
    Enrollment_Status:bool=False

class Term(TermBase):
    id:int=Field(primary_key=True)

    sections:list["Section"]=Relationship(back_populates="Term")