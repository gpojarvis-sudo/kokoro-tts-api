import os
import httpx

API_KEY = os.getenv("ELEVENLABS_API_KEY", "")
VOICE_ID = "CwhRBWXzGAHq8TQ4Fs17"


async def generate_voice(text: str):
    print("=" * 50)
    print("TEXT LENGTH:", len(text))
    print(text[:500])
    print("=" * 50)

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
