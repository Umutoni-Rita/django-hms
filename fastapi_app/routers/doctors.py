# app/routers/doctors.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, dependencies

router = APIRouter()

@router.post("/", response_model=schemas.DoctorResponse)
def create_doctor(doctor: schemas.DoctorBase, db: Session = Depends(dependencies.get_db)):
    return crud.create_doctor(db=db, doctor=doctor)

@router.get("/", response_model=list[schemas.DoctorResponse])
def get_doctors(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    return crud.get_doctors(db=db, skip=skip, limit=limit)
