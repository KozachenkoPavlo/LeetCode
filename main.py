import sys

from cli.commands.factories import build_command
from cli.errors import CliError
from config import Config


def main():
    args = sys.argv[1:]
    if not args:
        print("usage: main.py <command> [args...]", file=sys.stderr)
        return 2

    name, *rest = args
    try:
        command = build_command(name, Config.load())
    except CliError as error:
        print(error, file=sys.stderr)
        return 2

    command.execute(*rest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
