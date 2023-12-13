import pandas as pd
from datetime import datetime
from fastapi import UploadFile
from src.app.schemas import ProjectDTO, DataValueDTO, DataValueGet
from sqlalchemy.orm import Session
from src.app.crud import create_project, create_data_value


def file_to_db(db_session: Session, file_obj: UploadFile, import_id: int) -> None:
    df = pd.read_excel(io=file_obj.file, sheet_name="data", header=[0, 1])
    date_columns = [col for col in df.columns.levels[0] if isinstance(col, datetime)]

    # Замена пустых значений на 0
    for col in df.columns[2:]:
        df[col].fillna(0, inplace=True)

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


def db_to_file(data: list[DataValueGet], import_id: int) -> str:
    records = []
    for vd in data:
        temp_dict = {
            "Код": vd.project_rel.project_code,
            "Наименование проекта": vd.project_rel.project_name,
        }
        temp_dict[f"{vd.plan_date}_план"] = vd.plan_value
        temp_dict[f"{vd.fact_date}_факт"] = vd.fact_value
        records.append(temp_dict)
    df = pd.DataFrame(records)

    # Пока такой способ преобразовать из Decimal()
    for col in df.columns[2:]:
        df[col] = df[col].apply(
            lambda x: float(str(x).lstrip("[").rstrip("]")) if x else 0
        )

    df_grouped = (
        df.groupby(["Код", "Наименование проекта"])
        .agg(lambda x: x.dropna().tolist())
        .reset_index()
    )

    print(df_grouped)

    filename = f"file_version_{import_id}.xlsx"
    df_grouped.to_excel(filename, index=False)

    return filename
