from fastapi import APIRouter
from models.request import TTSRequest

router = APIRouter()


@router.post("/tts")
async def tts(req: TTSRequest):
    return {
        "success": True,
        "received_text": req.text,
        "length": len(req.text)
    }
