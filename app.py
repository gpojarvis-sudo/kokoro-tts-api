from fastapi import FastAPI
from models.request import TTSRequest

app = FastAPI()


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
