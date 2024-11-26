# app/main.py
from fastapi import FastAPI
from .routers import doctors, patients, appointments

app = FastAPI()

app.include_router(doctors.router, prefix="/api/doctors", tags=["Doctors"])
app.include_router(patients.router, prefix="/api/patients", tags=["Patients"])
app.include_router(appointments.router, prefix="/api/appointments", tags=["Appointments"])
@app.get("/test")
def test_endpoint():
    return {"message": "Hello World"}

