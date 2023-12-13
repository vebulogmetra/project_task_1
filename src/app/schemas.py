from pydantic import BaseModel, ConfigDict
from typing import Optional, Any
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


class DataValueGet(DataValueDTO):
    model_config = ConfigDict(from_attributes=True)
    import_rel: Optional[Any] = None
    project_rel: Optional[Any] = None


class StatusMsg(BaseModel):
    status: int
    detail: str
