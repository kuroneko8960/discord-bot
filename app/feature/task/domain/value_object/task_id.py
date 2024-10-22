from dataclasses import dataclass
from typing import ClassVar

@dataclass(frozen=True)
class TaskId:
    """値オブジェクト: タスクID"""
    value: int

    MIN_VALUE: ClassVar[int] = 1
    """最小値: 1"""

    MAX_VALUE: ClassVar[int] = 4294967295
    """最大値: 4294967295 (MySQLのUNSIGNED INTの最大値)"""


    def __init__(self, value: int) -> None:
        if value < self.MIN_VALUE:
            raise ValueError(f'タスクIDは{self.MIN_VALUE}以上の値を持つ必要があります')
        if value > self.MAX_VALUE:
            raise ValueError(f'タスクIDは{self.MAX_VALUE}以下の値を持つ必要があります')

        object.__setattr__(self, 'value', value)
