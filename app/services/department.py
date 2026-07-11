from app.schemas.department import DeptResponse, CreateDept,UpdateDept


class Department_Service:
    def __init__(self) -> None:
        pass

    def Create_Department(self, data: CreateDept) -> DeptResponse:
        return DeptResponse(
            id=1,
            dept_name="HR",
            dept_code=1,
        )

    def Get_Department(self) -> DeptResponse:
        return DeptResponse(
            id=1,
            dept_name="HR",
            dept_code=1,
        )

    def Patch_Department(self,data:UpdateDept)->DeptResponse:
        return DeptResponse(
            id=1,
            dept_name="HR",
            dept_code=1,
        )

    def Delete_Department(self)->DeptResponse:
        return DeptResponse(
            id=1,
            dept_name="HR",
            dept_code=1,
        )
    
Dept_Service=Department_Service()
