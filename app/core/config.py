from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Database settings
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_PORT: int

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@db:{self.DB_PORT}/{self.DB_NAME}"

    # API settings
    API_PREFIX: str 
    API_V1: str 
    DEBUG: bool 
    ALGORITHM: str 
    SECRET_KEY: str 
    ACCESS_TOKEN_EXPIRE_MINUTES: int 

    # Redis settings
    REDIS_HOST: str 
    REDIS_PORT: int 

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()