from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass(frozen=True)
class SubmissionSnapshot:
    difficulty: str
    count: int
    submissions: int

    def to_dict(self) -> dict:
        return {
            "difficulty": self.difficulty,
            "count": self.count,
            "submissions": self.submissions,
        }


@dataclass(frozen=True)
class UserProfile:
    username: str
    rank: int
    accepted_submissions: List[SubmissionSnapshot]
    total_submissions: List[SubmissionSnapshot]


@dataclass(frozen=True)
class RankSnapshot:
    date: date
    username: str
    rank: int
    accepted_submissions: List[SubmissionSnapshot]
    total_submissions: List[SubmissionSnapshot]

    def to_dict(self) -> dict:
        return {
            "date": self.date.isoformat(),
            "username": self.username,
            "rank": self.rank,
            "accepted_submissions": [submission.to_dict() for submission in self.accepted_submissions],
            "total_submissions": [submission.to_dict() for submission in self.total_submissions],
        }
