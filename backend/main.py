from fastapi import FastAPI

app = FastAPI(title="Neuro-X API")


@app.get("/")
def root():
    return {"message": "Neuro-X API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}