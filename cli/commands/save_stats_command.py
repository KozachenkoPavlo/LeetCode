from cli.commands import Command
from cli.models import RankSnapshot
from cli.repositories import ProfileRepository, UserStatisticRepository
from cli.services import UserStatisticService


class SaveStatisticCommand(Command):
    def __init__(
            self,
            profile_repository: ProfileRepository,
            statistic_repository: UserStatisticRepository,
    ):
        self.profile_repository = profile_repository
        self.statistic_repository = statistic_repository

    @staticmethod
    def __parce_username(*args):
        if not args:
            raise RuntimeError("Argument 'username' is expected")

        if len(args) != 1:
            raise RuntimeError("Expected only one argument, received {len(args)}")

        if not isinstance(args[0], str):
            raise RuntimeError("Expected argument 'username' of type 'str'")

        return args[0]

    def print_result(self, snapshot: RankSnapshot) -> None:
        print(f"Snapshot for user( {snapshot.username} ) was created with rank: {snapshot.rank}")

    def execute(self, *args) -> None:
        username = self.__parce_username(*args)
        service = UserStatisticService(self.profile_repository, self.statistic_repository)
        snapshot = service.save_statistic_for_today(username)

        self.print_result(snapshot)
