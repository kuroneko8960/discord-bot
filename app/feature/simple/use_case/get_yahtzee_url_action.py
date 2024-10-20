from base64 import encode
from typing import Optional
from app.shared.infrastructure.service.base64_service_interface import Base64ServiceInterface
from app.shared.infrastructure.service.env_service_interface import EnvServiceInterface
from app.shared.use_case.action_base import ActionBase


class GetYahtzeeUrlAction(ActionBase):
    """ヨットゲームのURLを取得するアクション"""

    def __init__(
        self,
        env_service: EnvServiceInterface,
        base64_service: Base64ServiceInterface
    ):
        self.env_service = env_service
        self.base64_service = base64_service


    def execute(self, room_name: Optional[str] = None) -> str:
        if room_name is None:
            room_name = self.env_service.get_env('YAHTZEE_ROOM_NAME') or ''

        encoded_room = self.base64_service.encode(room_name)

        return f"https://buddyboardgames.com/yahtzee?room={encoded_room}"

