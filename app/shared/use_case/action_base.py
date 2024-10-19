from typing import Any

from abc import ABC, abstractmethod


class ActionBase(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        pass