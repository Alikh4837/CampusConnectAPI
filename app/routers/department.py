from fastapi import APIRouter
from app.schemas.department import DeptResponse, CreateDept,UpdateDept
from app.services.department import Dept_Service
from app.models.department import Department

router = APIRouter(prefix="/departments", tags=["Departments"])


@router.post("/", response_model=DeptResponse)
async def Create_Department(data: CreateDept):
    return Dept_Service.Create_Department(data)

@router.get("/",response_model=DeptResponse)
async def Get_Department()->DeptResponse:
    department=Department(
        id=1,
        dept_name="HR",
        dept_code=1,
    )
    return DeptResponse(**department.model_dump())

@router.get("/list",response_model=list[DeptResponse])
async def List_Department()->list[DeptResponse]:
    departments=[
        Department(
        id=1,
        dept_name="HR",
        dept_code=1,
    ),
    Department(
        id=2,
        dept_name="HR",
        dept_code=1,
    )
    ]
    results:list[DeptResponse]=[]
    for department in departments:
        validated=DeptResponse(**department.model_dump())
        results.append(validated)
       
    return results

@router.patch("/",response_model=DeptResponse)
async def Patch_Department()->DeptResponse:
    department=Department(
        id=1,
        dept_name="HR",
        dept_code=1,
    )
    return DeptResponse(**department.model_dump())

@router.delete("/{id}",response_model=DeptResponse)
async def Delete_Department(id:int)->DeptResponse:
    department=Department(
        id=1,
        dept_name="HR",
        dept_code=1,
    )
    return DeptResponse(**department.model_dump())  