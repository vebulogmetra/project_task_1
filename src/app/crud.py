from src.app.models import Import, DataValue, Project
from sqlalchemy.orm import Session
from src.app.schemas import ImportDTO, ProjectDTO, DataValueDTO


def create_import(db: Session, import_data: ImportDTO):
    new_import = Import(**import_data.model_dump())
    db.add(new_import)
    db.commit()
    db.refresh(new_import)
    return new_import


def create_project(db: Session, project_data: ProjectDTO):
    new_project = Project(**project_data.model_dump())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


def create_data_value(db: Session, dv_data: DataValueDTO) -> None:
    new_dv = DataValue(**dv_data.model_dump())
    db.add(new_dv)
    db.commit()


def get_import_data(db: Session, import_id: int):
    return db.query(DataValue).filter(DataValue.import_id == import_id).all()
