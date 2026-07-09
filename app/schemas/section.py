from app.models.Section import SectionBase
from typing import Optional

class CreateSection(SectionBase):
    pass

class UpdateSection(SectionBase):
    section_name:Optional[str]

class SectionResponse(SectionBase):
    id:int