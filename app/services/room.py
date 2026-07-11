from app.schemas.room import RoomResponse,CreateRoom,UpdateRoom

class Room_Service:
    def __init__(self) -> None:
        pass
    def Post_Room(self,data:CreateRoom)->RoomResponse:
        return RoomResponse(
            id=1,
            occupied_status=False,
            room_num=1,
            building_num=1
        )
    def Get_Room(self)->RoomResponse:
        return RoomResponse(
            id=1,
            occupied_status=False,
            room_num=1,
            building_num=1
        )
    def Patch_Room(self,data:UpdateRoom)->RoomResponse:
        return RoomResponse(
            id=1,
            occupied_status=False,
            room_num=1,
            building_num=1
        )
    def Delete_Room(self)->RoomResponse:
        return RoomResponse(
            id=1,
            occupied_status=False,
            room_num=1,
            building_num=1
        )
    
room_service=Room_Service()