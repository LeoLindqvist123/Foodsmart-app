from pydantic_ai import Agent, BinaryContent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openrouter import OpenRouterProvider
from data_models import ScanResponse, RecipeResponse
from constants import MODEL, OPENROUTER_API_KEY

model = OpenAIChatModel(MODEL, provider=OpenRouterProvider(api_key=OPENROUTER_API_KEY))

scan_agent = Agent(
    model=model,
    output_type=ScanResponse,
    system_prompt="""You are a food identification assistant. You analyze photographs of refrigerators and list every food item you can see,
                  Work through the image systematically: top shelf to bottom shelf, then the door compartments, then the crisper drawers. Read product labels where they are visible.
                  Include items that are partially hidden or only partly visible. If you are uncertain what something is, 
                  include your best guess rather than omitting it — the user can correct the list afterwards.
                  Ignore anything that is not food or drink: cosmetics, medicine, cleaning products, packaging materials.
                  Give nutritional values per 100g as whole numbers.
                  Categories: fruit and vegetable are fresh produce. meat covers meat and poultry, fish covers fish and seafood. dairy is milk, cheese, yoghurt, butter and cream — 
                  but not eggs. bakery is bread and baked goods only, not dry pasta or rice. snacks is sweets and crisps. 
                  Everything else, including eggs, oils, condiments, pasta and rice, goes in other."""
)

recipe_agent = Agent(
    model=model,
    output_type=RecipeResponse,
    system_prompt="""You are a recipe assistant. Given a list of ingredients a user has at home, you suggest dishes they can cook,
            Prefer recipes that use what the user already has. You may include recipes that need one or two extra items,
            but list those in ingredients_missing — never in ingredients_available.
            Only list an ingredient as available if it appears in the user's list. Do not assume they have anything else, including basics like salt or oil.
            Give at most 10 recipes, and only ones that take 30 minutes or less. Write instructions as clear numbered steps. Give nutritional values per serving as 
            whole numbers, and cook_time_minutes as the total time from start to finish.{ingredient_list}"""
)

async def scan_image(image_bytes: bytes, media_type: str) -> ScanResponse:
    result = await scan_agent.run([
        "indentify all food in the picture",
        BinaryContent(data=image_bytes, media_type=media_type

        )
    ])
    return result.output

async def receive_recipe(ingredients: list[str]) -> RecipeResponse:
    ingredient_list = ", ".join(ingredients)
    result = await recipe_agent.run(
        f"Suggest recipes I can cook with these ingredients: {ingredient_list}",
    )
    return result.output