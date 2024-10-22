from dataclasses import dataclass
from typing import ClassVar

@dataclass(frozen=True)
class TaskContent:
    """値オブジェクト: タスク内容"""
    value: str

    MAX_LENGTH: ClassVar[int] = 30
    """最大文字数: 30"""

    def __init__(self, value: str) -> None:
        value = value.strip()

        if not value:
            raise ValueError('タスク内容は必ず指定してください')
        if len(value) > self.MAX_LENGTH:
            raise ValueError(f'タスク内容は{self.MAX_LENGTH}文字以下である必要があります')

        object.__setattr__(self, 'value', value)