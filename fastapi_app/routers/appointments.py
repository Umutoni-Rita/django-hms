# app/routers/appointments.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, dependencies

router = APIRouter()

@router.post("/", response_model=schemas.AppointmentResponse)
def create_appointment(appointment: schemas.AppointmentBase, db: Session = Depends(dependencies.get_db)):
    return crud.create_appointment(db=db, appointment=appointment)

@router.get("/", response_model=list[schemas.AppointmentResponse])
def get_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    return crud.get_appointments(db=db, skip=skip, limit=limit)
