# app/schemas.py
from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional

class GenderEnum(str, Enum):
    Male = "Male"
    Female = "Female"

class CategoryEnum(str, Enum):
    Internal_Medicine = "Internal_Medicine"
    Pediatrics = "Pediatrics"
    Gynecology = "Gynecology"
    Surgery = "Surgery"
    Laboratory = "Laboratory"
    Neonatology = "Neonatology"

class DoctorBase(BaseModel):
    first_name: str
    last_name: str
    category: CategoryEnum
    experience_years: int
    contact_number: Optional[str] = None
    email: str

class DoctorResponse(DoctorBase):
    id: int

    class Config:
        orm_mode = True

class PatientBase(BaseModel):
    first_name: str
    last_name: str
    gender: Optional[GenderEnum] = None
    date_of_birth: Optional[str] = None
    contact_number: Optional[str] = None
    email: str

class PatientResponse(PatientBase):
    id: int

    class Config:
        orm_mode = True

class AppointmentBase(BaseModel):
    
    patient_id: int
    doctor_id: int
    appointment_date: datetime
    reason: Optional[str] = None

class AppointmentResponse(AppointmentBase):
    id: int

    class Config:
        orm_mode = True
