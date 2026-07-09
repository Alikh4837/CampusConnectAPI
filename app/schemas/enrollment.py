from app.models.enrollment import EnrollmentBase
from typing import Optional

class CreateEnroll(EnrollmentBase):
    pass

class UpdateEnroll(EnrollmentBase):
    enrol_code:Optional[int]=None

class EnrollResponse(EnrollmentBase):
    id:int