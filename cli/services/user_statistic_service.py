from datetime import date

from cli.models.user_profile import RankSnapshot
from cli.repositories.profile_repository import ProfileRepository
from cli.repositories.user_statistic_repository import UserStatisticRepository


class UserStatisticService:
    def __init__(self, profile_repository: ProfileRepository, statistic_repository: UserStatisticRepository):
        self.profile_repository = profile_repository
        self.statistic_repository = statistic_repository

    def save_statistic_for_today(self, username: str):
        profile = self.profile_repository.get_profile_by_username(username)
        snapshot = RankSnapshot(
            date=date.today(),
            username=profile.username,
            rank=profile.rank,
            accepted_submissions=profile.accepted_submissions,
            total_submissions=profile.total_submissions,
        )
        self.statistic_repository.save(snapshot)

        return snapshot
