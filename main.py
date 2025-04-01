from fastapi import FastAPI
from app import upload, analyze

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Flohmarktscanner API is running!"}

app.include_router(upload.router)
app.include_router(analyze.router)
