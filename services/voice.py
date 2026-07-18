import os
import httpx

API_KEY = os.getenv("ELEVENLABS_API_KEY", "")


async def verify_connection():
    if not API_KEY:
        return {
            "success": False,
            "error": "ELEVENLABS_API_KEY not found"
        }

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
