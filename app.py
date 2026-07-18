from fastapi import FastAPI
from routers.tts import router as tts_router

app = FastAPI()


@app.get("/")
async def home():
    return {
        "status": "running"
    }


app.include_router(tts_router)
