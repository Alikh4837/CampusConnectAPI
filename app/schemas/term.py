from app.models.term import TermBase
from typing import Optional

class CreateTerm(TermBase):
    pass

class UpdateTerm(TermBase):
    Enrollment_Status:Optional[bool]=None

class TermResponse(TermBase):
    id:int