from app.schemas.scan import ScanResponse
from app.config import settings
from pydantic_ai import Agent, BinaryContent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openrouter import OpenRouterProvider

agent = Agent(
    model=settings.model_name,
    output_type=ScanResponse,
    system_prompt="You are an agent that scans food items and returns their nutritional information.",
)

async def scan_image(image_bytes: bytes) -> ScanResponse:
        result = await agent.run([
        "Identify all food items in this image.",
        BinaryContent(data=image_bytes, media_type="image/jpeg"),
    ])
        return result.output