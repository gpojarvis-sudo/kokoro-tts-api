def generate_voice(text: str):
    return {
        "success": True,
        "received_text": text,
        "length": len(text)
    }
