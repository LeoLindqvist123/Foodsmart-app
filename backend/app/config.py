from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openrouter_api_key: str
    model_name: str = "openai:gpt-4o-mini"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()