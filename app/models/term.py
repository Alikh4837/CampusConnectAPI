from sqlmodel import SQLModel, Field,Relationship
from typing import Optional,List,TYPE_CHECKING
from app.models.Section import Section

if TYPE_CHECKING:
    from app.models.Section import Section


class TermBase(SQLModel):
    Enrollment_Status:str=Field(index=True)

class Term(TermBase):
    id:int=Field(primary_key=True)

    sections:list["Section"]=Relationship(back_populates="Term")