from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TTSRequest(BaseModel):
    text: str


@app.get("/")
async def home():
    return {
        "status": "running"
    }


@app.post("/tts")
async def tts(req: TTSRequest):

    return {
        "success": True,
        "received_text": req.text,
        "length": len(req.text)
    }
