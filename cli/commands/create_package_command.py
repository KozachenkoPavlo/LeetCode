import os

from cli.commands.command import Command
from cli.repositories.leetcode_api_repository import LeetCodeAPIRepository
from cli.repositories.leetcode_repository import LeetCodeRepository
from cli.services.package_creator import PackageCreator


class CreatePackageCommand(Command):
    def __init__(self, leetcode_repository: LeetCodeRepository, package_creator: PackageCreator):
        self.leetcode_repository = leetcode_repository
        self.package_creator = package_creator

    @classmethod
    def create(cls) -> "CreatePackageCommand":
        return cls(
            leetcode_repository=LeetCodeAPIRepository(os.environ["LEET_CODE_API_URL"]),
            package_creator=PackageCreator(os.environ["ROOT_DIR"]),
        )

    @staticmethod
    def __parce_task_id(*args):
        if not args:
            raise RuntimeError("Argument 'task_id' is expected")

        try:
            return int(args[0])
        except ValueError as error:
            raise TypeError(f"Argument 'task_id' must be an integer, got '{args[0]}'") from error

    def execute(self, *args) -> None:
        task_id = self.__parce_task_id(*args)
        task = self.leetcode_repository.get_task_by_id(task_id)

        self.package_creator.create(task)
