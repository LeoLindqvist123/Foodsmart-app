from pydantic import BaseModel
from typing import Literal

class Ingredient(BaseModel):
    name: str
    calories: int
    protein_g: float
    carbohydrates_g: float 
    category: Literal["fruit", "vegetable", "grain", "protein", "dairy", "fat", "sugar", "beverage", "other"]

class ScanResponse(BaseModel):
    ingredients: list[Ingredient]
