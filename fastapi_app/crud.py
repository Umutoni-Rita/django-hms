# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def create_doctor(db: Session, doctor: schemas.DoctorBase):
    db_doctor = models.Doctor(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def get_doctors(db: Session, skip: int = 0, limit: int = None):
    query = db.query(models.Doctor)
    if limit:  # If a limit is set, use it, otherwise fetch all data
        query = query.offset(skip).limit(limit)
    return query.all()  


def create_patient(db: Session, patient: schemas.PatientBase):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patients(db: Session, skip: int = 0):
    
    patients = db.query(models.Patient).offset(skip).all()
    
    for patient in patients:
        if patient.date_of_birth:
            patient.date_of_birth = patient.date_of_birth.strftime('%Y-%m-%d')
            
    return patients

def create_appointment(db: Session, appointment: schemas.AppointmentBase):
    db_appointment = models.Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def get_appointments(db: Session, skip: int = 0, limit: int= None):
    return db.query(models.Appointment).offset(skip).all()

# def get_doctors(db: Session, skip: int = 0, limit: int = None):
#     query = db.query(models.Doctor)
#     if limit:  # If a limit is set, use it, otherwise fetch all data
#         query = query.offset(skip).limit(limit)
#     return query.all()  

