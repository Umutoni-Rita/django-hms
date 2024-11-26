# app/models.py
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class GenderEnum(enum.Enum):
    Male = "Male"
    Female = "Female"

class CategoryEnum(enum.Enum):
    Internal_Medicine = "Internal_Medicine"
    Pediatrics = "Pediatrics"
    Gynecology = "Gynecology"
    Surgery = "Surgery"
    Laboratory = "Laboratory"
    Neonatology = "Neonatology"

class Doctor(Base):
    __tablename__ = 'doctors_doctor'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    category = Column(Enum(CategoryEnum))
    experience_years = Column(Integer)
    contact_number = Column(String(15), nullable=True)
    email = Column(String, unique=True)

class Patient(Base):
    __tablename__ = 'patients_patient'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(Enum(GenderEnum), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    contact_number = Column(String(15), nullable=True)
    email = Column(String, unique=True)

class Appointment(Base):
    __tablename__ = 'appointments_appointment'
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients_patient.id'))
    doctor_id = Column(Integer, ForeignKey('doctors_doctor.id'))
    appointment_date = Column(DateTime)
    reason = Column(Text, nullable=True)

    patient = relationship("Patient")
    doctor = relationship("Doctor")
