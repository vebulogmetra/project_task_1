from fastapi import APIRouter, Depends, File, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from src.app import crud
from datetime import datetime
from src.utils.parser import process_file
from src.app.schemas import ImportDTO
import pandas as pd

router = APIRouter()


@router.post("/import_file/")
def import_file(
    file_: UploadFile = File(...), db_session: Session = Depends(crud.get_db)
):
    """ """

    import_data = ImportDTO(import_date=datetime.now(), file_name=file_.filename)
    new_import = crud.create_import(db=db_session, import_data=import_data)

    process_file(db_session=db_session, file_obj=file_, import_id=new_import.import_id)

    return status.HTTP_201_CREATED


@router.get("/export_file/{import_id}/")
def export_file(import_id: int, db_session: Session = Depends(crud.get_db)):
    data = crud.get_import_data(db=db_session, import_id=import_id)
    if not data:
        raise HTTPException(
            status_code=404, detail="Data for the specified version not found"
        )
    records = []
    for _, datavalue in data:
        temp_dict = {
            "Код": datavalue.project_rel.project_code,
            "Наименование проекта": datavalue.project_rel.project_name,
        }

        temp_dict[f"{datavalue.plan_date} план"] = datavalue.plan_value
        temp_dict[f"{datavalue.fact_date} факт"] = datavalue.fact_value
        records.append(temp_dict)
    df = pd.DataFrame(records)

    print(df)

    filename = f"file_version_{import_id}.xlsx"
    df.to_excel(filename, index=False)

    return {"filename": filename}
