from abc import ABC, abstractmethod
from typing import List

from cli.models.user_profile import RankSnapshot


class UserStatisticRepository(ABC):
    @abstractmethod
    def save(self, rank_snapshot: RankSnapshot) -> None:
        pass

    @abstractmethod
    def load(self, username: str) -> List[RankSnapshot]:
        pass
