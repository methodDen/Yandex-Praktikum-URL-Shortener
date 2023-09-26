import os

from logging import config as logging_config
from pydantic_settings import BaseSettings

from src.core.logger import LOGGING

logging_config.dictConfig(LOGGING)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class AppSettings(BaseSettings):
    app_title: str = "Url Shortener"
    database_dsn: str
    host: str = "127.0.0.1"
    port: int = 8080
    blacklist: list[str] = []

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


app_settings = AppSettings()