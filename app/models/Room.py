from sqlmodel import SQLModel, Field,Relationship
from typing import Optional,List,TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.section import Section


class RoomBase(SQLModel):
    occupied_status:bool=False
    room_num:int
    Building_num:int

class Room(RoomBase):
    id:int=Field(primary_key=True)

    sections:List["Section"]=Relationship(back_populates="Room")