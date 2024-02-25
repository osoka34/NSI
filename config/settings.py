from typing import Any, Dict, List

from pydantic import (
    AmqpDsn,
    AnyHttpUrl,
    BaseSettings,
    PostgresDsn,
    validator,
)


class Settings(BaseSettings):

    API: str = '/api'
    RPC: str = '/rpc'
    DOCS: str = '/docs'
    ADMIN: str = '/admin'
    STARTUP: str = 'startup'
    SHUTDOWN: str = 'shutdown'
    SECRET_KEY: str
    FLASK_ADMIN_SWATCH: str = 'cerulean'

    NAME: str = 'FastAPI Clean API'
    VERSION: str = '1.0'
    DESCRIPTION: str = 'FastAPI Clean REST API'

    SWAGGER_UI_PARAMETERS: Dict[str, Any] = {
        'displayRequestDuration': True,
        'filter': True,
    }

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator('BACKEND_CORS_ORIGINS', pre=True)
    def assemble_cors_origins(
        cls, value: str | List[str],  # noqa: N805, WPS110
    ) -> str | List[str]:
        if isinstance(value, str) and not value.startswith('['):
            return [i.strip() for i in value.split(',')]
        elif isinstance(value, (list, str)):
            return value

        raise ValueError(value)

    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DATABASE_URI: PostgresDsn | None = None

    @validator('DATABASE_URI', pre=True)
    def assemble_db_connection(
        cls, value: str | None, values: Dict[str, Any],  # noqa: N805, WPS110
    ) -> str:
        if isinstance(value, str):
            return value

        return PostgresDsn.build(
            scheme='postgresql+asyncpg',
            user=values.get('DB_USER'),
            password=values.get('DB_PASSWORD'),
            host=values.get('DB_HOST'),
            port=values.get('DB_PORT'),
            path='/{0}'.format(values.get('DB_NAME')),
        )
    class Config(object):
        case_sensitive = True


# settings = Settings()