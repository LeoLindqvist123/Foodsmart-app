from fastapi import FastAPI

app = FastAPI(title="FoodSmart API", description="API for FoodSmart application", version="0.1.0")

@app.get("/health")
async def health():
    return {"status": "healthy"}