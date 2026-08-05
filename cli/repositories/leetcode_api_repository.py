import requests

from cli.errors import ObjectNotFoundError, LeetCodeError
from cli.models import Task, UserProfile, SubmissionSnapshot
from cli.repositories.profile_repository import ProfileRepository
from cli.repositories.task_repository import TaskRepository


class LeetCodeAPIRepository(TaskRepository, ProfileRepository):
    def __init__(self, api_url: str):
        self.base_url = api_url

    def _get(self, path: str) -> dict:
        try:
            response = requests.get(f"{self.base_url}{path}", timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as error:
            if error.response.status_code == 404:
                raise ObjectNotFoundError(path) from error
            raise LeetCodeError(f"LeetCode returned {error.response.status_code}") from error
        except requests.RequestException as error:
            raise LeetCodeError("Could not reach LeetCode") from error

    def _task_from_api(self, data: dict) -> Task:
        return Task(
            id=data["questionId"],
            frontend_id=data["questionFrontendId"],
            title=data["title"],
            difficulty=data["difficulty"],
            tags=[tag["name"] for tag in data["topicTags"]],
        )

    def _profile_from_api(self, data: dict) -> UserProfile:
        return UserProfile(
            username=data["username"],
            rank=data["profile"]["ranking"],
            accepted_submissions=[SubmissionSnapshot(
                difficulty=submission["difficulty"],
                count=submission["count"],
                submissions=submission["submissions"],
            ) for submission in data["submitStats"]["acSubmissionNum"]],
            total_submissions=[SubmissionSnapshot(
                difficulty=submission["difficulty"],
                count=submission["count"],
                submissions=submission["submissions"],
            ) for submission in data["submitStats"]["totalSubmissionNum"]],
        )

    def get_task_by_id(self, task_id: int) -> Task:
        path = f"/problem/{task_id}"

        return self._task_from_api(self._get(path))

    def get_profile_by_username(self, username: str) -> UserProfile:
        path = f"/user/{username}"

        return self._profile_from_api(self._get(path))
