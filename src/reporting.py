from src.settings import settings
from abc import ABC, abstractmethod


class reporting(ABC):
    def __init__(self, settings: settings):
        self.settings = settings

    @abstractmethod
    def create(self, key: str) -> str:
        return ""

    @staticmethod
    @abstractmethod
    def unit_key() -> str:
        pass

    @staticmethod
    @abstractmethod
    def group_key() -> str:
        pass

    @staticmethod
    @abstractmethod
    def nomenclature_key() -> str:
        pass