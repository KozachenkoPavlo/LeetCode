from abc import ABC, abstractmethod

from cli.models.task import Task


class TaskRepository(ABC):
    @abstractmethod
    def get_task_by_id(self, task_id: int) -> Task:
        pass
