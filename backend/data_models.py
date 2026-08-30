from pydantic import BaseModel
from typing import Literal

class Ingredients(BaseModel):
    name: str
    calories: int
    protein_g: int
    carbohydrates_g: float

    category: Literal["fruit", "vegetable", "meat", "fish", "dairy", "bakery", "snacks", "vegan"]

class ScanResponse(BaseModel):
    ingredients: list[Ingredients]
