from abc import ABC, abstractmethod

class EnvServiceInterface(ABC):
    @abstractmethod
    def get_env(self, env_name: str) -> str | None:
        """環境変数を取得します"""
        pass