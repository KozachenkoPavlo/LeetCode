from abc import abstractmethod, ABC


class LeetCodeRepository(ABC):
    @abstractmethod
    def get_task_by_id(self, task_id: int):
        pass
