from pydantic_ai import Agent
from app.schemas.scan import ScanResponse
from app.config import settings

agent = Agent(
    model=settings.model_name,
    output_type=ScanResponse,
    system_prompt="You are an agent that scans food items and returns their nutritional information.",
)