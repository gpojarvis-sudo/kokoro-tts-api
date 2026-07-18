from fastapi import APIRouter
from models.request import TTSRequest
from services.voice import generate_voice

router = APIRouter()


@router.post("/tts")
async def tts(req: TTSRequest):
    return generate_voice(req.text)
