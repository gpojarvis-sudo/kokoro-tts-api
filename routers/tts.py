from fastapi import APIRouter
from fastapi.responses import Response
from models.request import TTSRequest
from services.voice import generate_voice

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
