from app.shared.use_case.action_base import ActionBase


class PingAction(ActionBase):
    def execute(self) -> str:
        return "にゃ！"