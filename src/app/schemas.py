from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ImportDTO(BaseModel):
    import_date: datetime
    file_name: str


class ProjectDTO(BaseModel):
    project_code: int
    project_name: str


class DataValueDTO(BaseModel):
    import_id: Optional[int] = None
    project_id: Optional[int] = None
    plan_date: datetime
    plan_value: float
    fact_date: datetime
    fact_value: float
