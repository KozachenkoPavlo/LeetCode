from abc import abstractmethod, ABC


class Command(ABC):
    @classmethod
    @abstractmethod
    def create(cls) -> "Command":
        pass

    @abstractmethod
    def execute(self, *args) -> None:
        pass
