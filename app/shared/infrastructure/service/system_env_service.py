import os

from app.shared.infrastructure.service.env_service_interface import EnvServiceInterface


class SystemEnvService(EnvServiceInterface):
    """システムから環境変数を取得するサービス"""

    def get_env(self, env_name: str) -> str | None:
        return os.getenv(env_name)