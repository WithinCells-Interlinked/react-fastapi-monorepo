from fastapi import FastAPI

app = FastAPI(
    title="Molt's Monorepo API",
    description="A foundational API built with FastAPI, managed autonomously.",
    version="0.0.1",
)

@app.get("/")
async def root():
    return {"message": "System online. Standing by."}

@app.get("/health")
async def health_check():
    return {"status": "ok"}
