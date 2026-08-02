from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class UserProfile:
    username: str
    rank: int


@dataclass(frozen=True)
class RankSnapshot:
    date: date
    username: str
    rank: int

    def to_dict(self) -> dict:
        return {
            "date": self.date.isoformat(),
            "username": self.username,
            "rank": self.rank,
        }
