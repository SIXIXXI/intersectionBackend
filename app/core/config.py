from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

  SECRET_KEY: str = "secret"
  DATABASE_URL: str = "db_url"

  PROJECT_NAME: str = "FastAPI"


settings = Settings()
