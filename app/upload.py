from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter()

@router.post('/upload')
async def upload_image(file: UploadFile = File(...)):
    upload_folder = 'uploads'
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, file.filename)
    with open(file_path, 'wb') as f:
        f.write(await file.read())
    return {"message": f"Bild empfangen – Dateiname: {file.filename}"}
