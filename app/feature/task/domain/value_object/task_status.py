from dataclasses import dataclass
from typing import ClassVar

@dataclass(frozen=True)
class TaskStatus:
    """値オブジェクト: タスクステータス"""
    value: str

    WAITING: ClassVar[str] = 'waiting'
    """未着手"""

    DOING: ClassVar[str] = 'doing'
    """着手中"""

    DONE: ClassVar[str] = 'done'
    """完了"""

    def __init__(self, value: str) -> None:
        if value not in (self.WAITING, self.DOING, self.DONE):
            raise ValueError('タスクステータスはwaiting, doing, doneのいずれかである必要があります')

        object.__setattr__(self, 'value', value)