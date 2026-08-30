from pydantic_ai import Agent, BinaryContent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openrouter import OpenRouterProvider
from data_models import ScanResponse
from constants import MODEL, OPENROUTER_API_KEY

model = OpenAIChatModel(MODEL, provider=OpenRouterProvider(api_key=OPENROUTER_API_KEY))

agent = Agent(
    model=model,
    output_type=ScanResponse,
    system_prompt="You are an ai agent that scans fridges, and say what foods is in the fridge"
)

async def scan_image(image_bytes: bytes) -> ScanResponse:
    result = await agent.run([
        "indentify all food in the picture",
        BinaryContent(data=image_bytes, media_type="image/jpeg")
    ])
    return result.output