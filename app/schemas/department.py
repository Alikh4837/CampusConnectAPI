from app.models.department import DepartmentBase
from typing import Optional

class CreateDept(DepartmentBase):
    pass

class UpdateDept(DepartmentBase):
    dname:Optional[str]=None
    dcode:Optional[int]=None

class DeptResponse(DepartmentBase):
    id:int