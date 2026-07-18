import os
import httpx

API_KEY = os.getenv("ELEVENLABS_API_KEY", "")
VOICE_ID = "CwhRBWXzGAHq8TQ4Fs17"


async def verify_connection():
    headers = {
        "xi-api-key": API_KEY
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.elevenlabs.io/v1/voices",
            headers=headers
        )

    return {
        "status_code": response.status_code,
        "response": response.json()
    }


async def generate_voice(text: str):
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2"
    }

    async with httpx.AsyncClient(timeout=120) as client:
        response = await client.post(
            f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}",
            headers=headers,
            json=payload
        )

    response.raise_for_status()

    return response.content
