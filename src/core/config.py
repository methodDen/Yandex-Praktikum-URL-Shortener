from pydantic import (
    BaseSettings,
    PostgresDsn,
)


class AppSettings(BaseSettings):
    app_name: str = "Url Shortener"
    database_dsn: PostgresDsn

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


app_settings = AppSettings()