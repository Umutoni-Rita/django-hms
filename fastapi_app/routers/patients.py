# app/routers/patients.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, dependencies

router = APIRouter()

@router.post("/", response_model=schemas.PatientResponse)
def create_patient(patient: schemas.PatientBase, db: Session = Depends(dependencies.get_db)):
    return crud.create_patient(db=db, patient=patient)

@router.get("/", response_model=list[schemas.PatientResponse])
def get_patients(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    return crud.get_patients(db=db, skip=skip, limit=limit)
