from enum import Enum

from pydantic_settings import BaseSettings, SettingsConfigDict


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    ERROR = "ERROR"


class Settings(BaseSettings):
    log_level: LogLevel
    http_port: int

    model_config = SettingsConfigDict(env_file=".env")
