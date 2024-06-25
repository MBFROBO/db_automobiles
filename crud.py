from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, exc
import models

def create(db:Session, base_key:str, id:int, brand:str, model:str, year:str, program_data:str):
    _db = models.SHEET_NAME[base_key](
        id=id,
        brand=brand,
        model=model, 
        year=year, 
        program_data=program_data
    )
    db.add(_db)
    db.commit()
    db.refresh(_db)
    return _db

def read_all(db:Session):
    return db.query(models.SHEET_NAME[models.SHEET_NAME.id]).all()