from dataclasses import dataclass
from typing import List


@dataclass
class Task:
    id: str
    frontend_id: str
    title: str
    difficulty: str
    tags: List[str]
