from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "AI Video Factory API Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
