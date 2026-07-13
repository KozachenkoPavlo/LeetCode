import requests

from cli.repositories.leetcode_repository import LeetCodeRepository
from cli.models.task import Task


class LeetCodeAPIRepository(LeetCodeRepository):
    base_url: str

    def __init__(self, api_url: str):
        self.base_url = api_url

    def get_task_by_id(self, task_id: int) -> Task:
        url = f"{self.base_url}/problem/{task_id}"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"Status code is {response.status_code}")

        data = response.json()

        return Task(
            id=data["questionId"],
            frontend_id=data["questionFrontendId"],
            title=data["title"],
            difficulty=data["difficulty"],
            tags=[tag["name"] for tag in data["topicTags"]],
        )
