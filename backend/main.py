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

# Autonomous commit performed at: Wed 18 Feb 22:00:01 -03 2026

# Autonomous commit performed at: Thu 19 Feb 10:00:01 -03 2026
