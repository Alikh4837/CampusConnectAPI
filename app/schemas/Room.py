from app.models.Room import RoomBase
from typing import Optional

class CreateRoom(RoomBase):
    pass

class UpdateRoom(RoomBase):
    occupied_status:Optional[bool]=False
    room_num:Optional[int]=None
    Building_num:Optional[int]=None

class RoomResponse(RoomBase):
    id:int