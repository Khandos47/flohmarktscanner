from fastapi import APIRouter

router = APIRouter()

@router.get('/analyze/{filename}')
async def analyze_image(filename: str):
    # Dummy-Analyse: Hier könnte echte Bilderkennung laufen
    return {
        "filename": filename,
        "erkannter_artikel": "Altes Lego-Set",
        "geschätzter_wert": "25 €"
    }
