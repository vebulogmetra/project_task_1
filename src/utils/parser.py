import pandas as pd
from datetime import datetime
from fastapi import UploadFile
from src.app.schemas import ProjectDTO, DataValueDTO
from sqlalchemy.orm import Session
from src.app.crud import create_project, create_data_value


def process_file(db_session: Session, file_obj: UploadFile, import_id: int) -> None:
    df = pd.read_excel(io=file_obj.file, sheet_name="data", header=[0, 1])
    date_columns = [col for col in df.columns.levels[0] if isinstance(col, datetime)]

    for _, row in df.iterrows():
        project_data = ProjectDTO(
            project_code=row[("Unnamed: 0_level_0", "Код")],
            project_name=row[("Unnamed: 1_level_0", "Наименование проекта")],
        )

        new_project = create_project(db=db_session, project_data=project_data)

        for date_col in date_columns:
            data_value = DataValueDTO(
                import_id=import_id,
                project_id=new_project.project_id,
                plan_date=date_col,
                plan_value=row[(date_col, "план")],
                fact_date=date_col,
                fact_value=row[(date_col, "факт")],
            )
            create_data_value(db=db_session, dv_data=data_value)
