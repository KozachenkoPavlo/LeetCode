import os
from typing import List

from cli.models.task import Task


class PackageCreator:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir

    def create(self, task: Task) -> None:
        package_path = self._package_path(task)

        os.makedirs(package_path)
        self._create_init_file(package_path, task.tags)
        self._create_solution_file(package_path)

    def _difficulty_path(self, task: Task) -> str:
        return os.path.join(self.root_dir, task.difficulty.lower())

    def _package_name(self, task: Task) -> str:
        clear_title = task.title.lower().replace(".", "").replace(" ", "_")

        return "_".join([task.frontend_id, clear_title])

    def _package_path(self, task: Task) -> str:
        return os.path.join(self._difficulty_path(task), self._package_name(task))

    def _create_init_file(self, package_path: str, tags: List[str]) -> None:
        content = "tags = [\n"
        content += "\n".join([f"    \"{tag}\"," for tag in tags])
        content += "\n]\n"

        with open(os.path.join(package_path, "__init__.py"), "w") as file:
            file.write(content)

    def _create_solution_file(self, package_path: str) -> None:
        with open(os.path.join(package_path, "solution_1.py"), "w") as file:
            file.write("")
