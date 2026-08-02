from abc import abstractmethod, ABC


class Command(ABC):
    @abstractmethod
    def execute(self, *args) -> None:
        pass
