from fastapi import APIRouter
from models.request import TTSRequest
from services.voice import generate_voice, verify_connection

router = APIRouter()

@router.post("/tts")
async def tts(req: TTSRequest):
    return await generate_voice(req.text)

@router.get("/verify")
async def verify():
    return await verify_connection()
