from fastapi import APIRouter
from fastapi.responses import Response
from models.request import TTSRequest
from services.voice import generate_voice, verify_connection

router = APIRouter()

@router.post("/tts")
async def tts(req: TTSRequest):

    audio = await generate_voice(req.text)

    return Response(
        content=audio,
        media_type="audio/mpeg",
        headers={
            "Content-Disposition": "inline; filename=voice.mp3"
        }
    )

@router.get("/verify")
async def verify():
    return await verify_connection()
