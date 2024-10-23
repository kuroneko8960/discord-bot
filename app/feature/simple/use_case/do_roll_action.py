import random

from app.shared.use_case.action_base import ActionBase

class DoRollAction(ActionBase):
    def execute(self) -> int:
        return random.randrange(100)