from fastapi import FastAPI, UploadFile, File
from data_models import ScanResponse
from agents import scan_image

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/scan", response_model=ScanResponse)
async def scan_image_endpoint(file: UploadFile = File(...)):
    image_bytes = await file.read()
    return await scan_image(image_bytes, file.content_type)