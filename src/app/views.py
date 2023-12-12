from fastapi import APIRouter, Depends
from src.utils.database import get_db

router = APIRouter()


@router.get("/")
def get__(db_session: Session = Depends(get_db)):
    """ """
