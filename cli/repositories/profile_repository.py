from abc import ABC, abstractmethod

from cli.models.user_profile import UserProfile


class ProfileRepository(ABC):
    @abstractmethod
    def get_profile_by_username(self, username: str) -> UserProfile:
        pass
