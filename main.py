import sys

from env import init_env
from cli.commands.command_loader import load_command


def main():
    init_env()
    command_name, *args = sys.argv[1:]

    command = load_command(command_name)
    command.execute(*args)


if __name__ == "__main__":
    main()
