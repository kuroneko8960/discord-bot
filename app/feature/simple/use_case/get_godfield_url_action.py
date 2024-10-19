from typing import Optional, Tuple
from app.shared.infrastructure.service.env_service_interface import EnvServiceInterface
from app.shared.use_case.action_base import ActionBase


class GetGodfieldUrlResponse:
    def __init__(self, url: str, passphrase: str):
        self.url = url
        self.passphrase = passphrase


class GetGodfieldUrlAction(ActionBase):
    def __init__(self, env_service: EnvServiceInterface):
        self.env_service = env_service


    def execute(self, passphrase: Optional[str] = None) -> GetGodfieldUrlResponse:
        """ゴッドフィールドのURLと合言葉を取得する"""
        if passphrase is None:
            passphrase = self.env_service.get_env('GODFIELD_PASSPHRASE')

        if passphrase is None:
            raise ValueError("デフォルトの合言葉が設定されていません")

        return GetGodfieldUrlResponse(
            url="https://godfield.net",
            passphrase=passphrase
        )