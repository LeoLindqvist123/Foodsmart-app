from pydantic import BaseModel
from typing import Literal

class Ingredient(BaseModel):
    name: str
    calories: int
    protein_g: int
    carbohydrates_g: int

    category: Literal["fruit", "vegetable", "meat", "fish", "dairy", "bakery", "snacks", "other"]

class ScanResponse(BaseModel):
    ingredients: list[Ingredient]


class Recipe(BaseModel):
    name: str
    instructions: list[str]
    ingredients_missing: list[str]
    ingredients_available: list[str]
    calories: int
    protein_g: int
    carbohydrates_g: int

class RecipeResponse(BaseModel):
    recipes: list[Recipe]