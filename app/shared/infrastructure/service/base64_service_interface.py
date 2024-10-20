from abc import ABC, abstractmethod


class Base64ServiceInterface(ABC):
    @abstractmethod
    def encode(self, value: str) -> str:
        pass