import json
import os
from datetime import date
from io import TextIOWrapper
from typing import List

from cli.models.user_profile import RankSnapshot
from cli.repositories.user_statistic_repository import UserStatisticRepository


class JsonUserStatisticRepository(UserStatisticRepository):
    def __init__(self, root_dir: str):
        self.root_dir = root_dir

    def _directory(self) -> str:
        return os.path.join(self.root_dir, "out", "rank")

    def _filename(self, username: str) -> str:
        return os.path.join(self._directory(), f"{username}.json")

    def _load_raw(self, username: str) -> list:
        try:
            with open(self._filename(username), "r") as file:
                statistics = json.load(file)
        except FileNotFoundError as error:
            return []

        return statistics

    def load(self, username: str) -> List[RankSnapshot]:
        result = []

        for statistic in self._load_raw(username):
            result.append(RankSnapshot(
                username=statistic["username"],
                rank=statistic["rank"],
                date=date.fromisoformat(statistic["date"]),
            ))

        return result

    def save(self, snapshot: RankSnapshot) -> None:
        statistics = self.load(snapshot.username)

        for statistic in statistics:
            if statistic.date == snapshot.date:
                return

        statistics.append(snapshot)
        statistics.sort(key=lambda element: element.date)

        filename = self._filename(snapshot.username)
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "w") as file:
            file: TextIOWrapper
            json.dump([statistic.to_dict() for statistic in statistics], file, indent=2)
