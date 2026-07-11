from fastapi import APIRouter
from app.schemas.instructor import InstructorResponse,CreateInstructor
from app.services.instructor import instructor_service
from app.models.instructor import Instructor


router=APIRouter(
    prefix="/instructors",
    tags=["Instructors"]
)

@router.post("/",response_model=InstructorResponse)
def Create_Instructor(data:CreateInstructor):
    return instructor_service.Post_Instructor(data)

@router.get("/",response_model=InstructorResponse)
def Get_Instructor()->InstructorResponse:
    instructor=Instructor(  
         id=1,
            name="Prof.Ahmed",
            phone="+92 398 898379",
            address="Johar town",
            password="not a password",
            emergency_contact="+92 398 892372",
    )
    return InstructorResponse(**instructor.model_dump())

@router.get("/list",response_model=list[InstructorResponse])
async def list_instructors()->list[InstructorResponse]:
    instructors=[
        Instructor(
             id=1,
            name="Prof.Ahmed",
            phone="+92 398 898379",
            address="Johar town",
            password="not a password",
            emergency_contact="+92 398 892372",
        ),
        Instructor(
             id=2,
            name="Prof.Ahmed",
            phone="+92 398 898379",
            address="Johar town",
            password="not a password",
            emergency_contact="+92 398 892372",
        ),
    ]
    results:list[InstructorResponse]=[]
    for instructor in instructors:
        validated=InstructorResponse(**instructor.model_dump())
        results.append(validated)

    return results

@router.patch("/",response_model=InstructorResponse)
async def update_instructor()->InstructorResponse:
    instructor=Instructor(
             id=1,
            name="Prof.Ahmed",
            phone="+92 398 898379",
            address="Johar town",
            password="not a password",
            emergency_contact="+92 398 892372",
        )
    return InstructorResponse(**instructor.model_dump())

@router.delete("/{id}",response_model=InstructorResponse)
async def delete_instructor(id:int)->InstructorResponse:
    instructor=Instructor(
             id=1,
            name="Prof.Ahmed",
            phone="+92 398 898379",
            address="Johar town",
            password="not a password",
            emergency_contact="+92 398 892372",
        )
    return InstructorResponse(**instructor.model_dump())