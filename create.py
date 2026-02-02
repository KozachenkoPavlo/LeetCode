import argparse
import os
from enum import Enum


class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


def create_leetcode_package(task_name: str, difficulty: Difficulty):
    base_path = os.path.join(os.getcwd(), difficulty.value, task_name)
    os.makedirs(base_path, exist_ok=True)

    with open(os.path.join(base_path, "__init__.py"), "w") as file:
        file.write("tags = []\n")

    with open(os.path.join(base_path, "solution_1.py"), "w") as file:
        file.write("")


def main():
    parser = argparse.ArgumentParser(description="Create a package for LeetCode task")

    parser.add_argument("task_name")

    parser.add_argument_group("Task difficulty")
    parser.add_argument("-e", "--easy", action="store_true", help="Mark task as easy")
    parser.add_argument("-m", "--medium", action="store_true", help="Mark task as medium")
    parser.add_argument("-d", "--hard", action="store_true", help="Mark task as hard")

    args = parser.parse_args()

    task_name = args.task_name
    task_name = task_name.lower().replace(".", "").replace(" ", "_")

    if args.easy:
        difficulty = Difficulty.EASY
    elif args.medium:
        difficulty = Difficulty.MEDIUM
    elif args.hard:
        difficulty = Difficulty.HARD
    else:
        difficulty = Difficulty.EASY

    create_leetcode_package(task_name, difficulty)


if __name__ == "__main__":
    main()
