from typing import Any

from abc import ABC, abstractmethod


class ControllerBase(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        pass