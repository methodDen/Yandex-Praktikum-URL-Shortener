import os

from pydantic import (
    PostgresDsn,
    HttpUrl,
)
from pydantic_settings import BaseSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class AppSettings(BaseSettings):
    app_title: str = "Url Shortener"
    database_dsn: str
    host: str = "127.0.0.1"
    port: int = 8080

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


app_settings = AppSettings()