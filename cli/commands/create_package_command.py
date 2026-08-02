from cli.commands import Command
from cli.errors import PackageAlreadyExistsError
from cli.repositories import TaskRepository
from cli.services import PackageCreatorService


class CreatePackageCommand(Command):
    def __init__(self, repository: TaskRepository, package_creator: PackageCreatorService):
        self.repository = repository
        self.package_creator = package_creator

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
        task = self.repository.get_task_by_id(task_id)

        try:
            self.package_creator.create(task)
        except PackageAlreadyExistsError:
            print(f"Package for task(ID: {task.frontend_id}) was already created")
