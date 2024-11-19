from fastapi import FastAPI

app = FastAPI()

@app.get("/fastapi")
async def read_root():
    return {"message": "Welcome to FastAPI in the HMS project!"}
