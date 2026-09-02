from fastapi import FastAPI, UploadFile, File
from data_models import ScanResponse, RecipeResponse, RecipeRequest
from agents import scan_image, receive_recipe

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/scan", response_model=ScanResponse)
async def scan_image_endpoint(file: UploadFile = File(...)):
    image_bytes = await file.read()
    return await scan_image(image_bytes, file.content_type)

@app.post("/recipes", response_model=RecipeResponse)
async def recipes(request: RecipeRequest):
    result = await receive_recipe(request.ingredients)
    return result