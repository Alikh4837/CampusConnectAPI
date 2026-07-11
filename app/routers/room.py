from fastapi import APIRouter
from app.schemas.room import RoomResponse,CreateRoom
from app.services.room import room_service
from app.models.room import Room

router = APIRouter(
    prefix="/rooms",
    tags=["Rooms"]
)

@router.post("/",response_model=RoomResponse)
async def Create_Room(data:CreateRoom):
    return room_service.Post_Room(data)

@router.get("/",response_model=RoomResponse)
async def Get_Room()->RoomResponse:
    room=Room(
        id=1,
            occupied_status=False,
            room_num=1,
            building_num=1
    )
    return RoomResponse(**room.model_dump())

@router.get("/list",response_model=RoomResponse)
async def Get_list()->list[RoomResponse]:
    Rooms=[Room(
        id=1,
        occupied_status=False,
        room_num=1,
        building_num=1
    ),
    Room(
        id=2,
        occupied_status=False,
        room_num=2,
        building_num=2
    )
    ]
    results:list[RoomResponse]=[]
    for room in Rooms:
        validated=RoomResponse(**room.model_dump())
        results.append(validated)
    
    return results

@router.patch("/{id}",response_model=RoomResponse)
async def Patch_Room(id:int)->RoomResponse:
    room=Room(
        id=1,
            occupied_status=False,
            room_num=1,
            building_num=1
    )
    return RoomResponse(**room.model_dump())

@router.delete("/{id}",response_model=RoomResponse)
async def Delete_Room(id:int)->RoomResponse:
    room=Room(
        id=1,
            occupied_status=False,
            room_num=1,
            building_num=1
    )
    return RoomResponse(**room.model_dump())