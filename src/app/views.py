from datetime import datetime

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from pydantic import ValidationError
from sqlalchemy.orm import Session

from src.app import crud
from src.app.schemas import DataValueGet, ImportDTO, StatusMsg
from src.utils.database import get_db
from src.utils.parser import db_to_file, file_to_db

router = APIRouter()


@router.post("/import_file/", response_model=StatusMsg)
def import_file(file_: UploadFile = File(...), db_session: Session = Depends(get_db)):
    import_data = ImportDTO(import_date=datetime.now(), file_name=file_.filename)
    new_import = crud.create_import(db=db_session, import_data=import_data)

    file_to_db(db_session=db_session, file_obj=file_, import_id=new_import.import_id)

    return StatusMsg(status=201, detail="File import successful")


@router.get("/export_file/{import_id}/", response_model=StatusMsg)
def export_file(import_id: int, db_session: Session = Depends(get_db)):
    db_data = crud.get_import_data(db=db_session, import_id=import_id)
    if not db_data:
        raise HTTPException(status_code=404, detail="Data for the import_id not found")

    try:
        data = [DataValueGet.model_validate(d) for d in db_data]
    except ValidationError as e:
        print(f"PARSE MODEL ERROR: {e}")
        raise HTTPException(status_code=500, detail="Internav server error")

    filename: str = db_to_file(data=data, import_id=import_id)

    return StatusMsg(status=200, detail=f"Filename: {filename}")
