from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=['.env', '../.env', '../../.env'], env_file_encoding='utf-8')

    google_sheets_url: str = ''

settings = Settings()
