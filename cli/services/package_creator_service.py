import os
import re
import shutil
from typing import List

from cli.errors import PackageAlreadyExistsError
from cli.models.task import Task


class PackageCreatorService:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir

    def create(self, task: Task) -> None:
        package_path = self._package_path(task)

        try:
            os.makedirs(package_path)
        except FileExistsError as error:
            raise PackageAlreadyExistsError(f"Task(ID: {task.frontend_id}) is already created") from error

        try:
            self._create_init_file(package_path, task.tags)
            self._create_solution_file(package_path)
        except Exception:
            shutil.rmtree(package_path, ignore_errors=True)
            raise

    def _difficulty_path(self, task: Task) -> str:
        return os.path.join(self.root_dir, task.difficulty.lower())

    def _package_name(self, task: Task) -> str:
        slug = re.sub(r"[^a-z0-9]+", "_", task.title.lower()).strip("_")

        return f"{task.frontend_id}_{slug}"

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
