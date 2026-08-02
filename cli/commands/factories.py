from typing import Dict, Callable

from cli.commands import Command, CreatePackageCommand, SaveStatisticCommand
from cli.errors import UnknownCommandError
from cli.repositories.json_user_statistic_repository import JsonUserStatisticRepository
from cli.repositories.leetcode_api_repository import LeetCodeAPIRepository
from cli.services import PackageCreatorService
from config import Config


def build_command(name: str, config: Config) -> Command:
    leetcode = LeetCodeAPIRepository(config.leetcode_api_url)
    statistic = JsonUserStatisticRepository(config.root_dir)

    package_creator = PackageCreatorService(config.root_dir)

    factories: Dict[str, Callable[[], Command]] = {
        "create": lambda: CreatePackageCommand(leetcode, package_creator),
        "save_statistic": lambda: SaveStatisticCommand(leetcode, statistic),
    }

    try:
        factory = factories[name]
    except KeyError as error:
        available = ", ".join(sorted(factories))
        raise UnknownCommandError(f"Unknown command '{name}'. Available: {available}") from error

    return factory()
