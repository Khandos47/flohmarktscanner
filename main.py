from fastapi import FastAPI
from app import upload

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Flohmarktscanner API is running!"}

app.include_router(upload.router)
