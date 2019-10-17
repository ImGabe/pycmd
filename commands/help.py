from importlib import import_module
from pathlib import Path


currentDirectory = Path("commands")


def run(args: list) -> None:
    try:
        if args:
            print(f"{args[0]}: {import_module(f'commands.{args[0]}').help()}")
            return
    except ModuleNotFoundError:
        print(f"Invalid command: {args[0]}")
        return
    except AttributeError:
        print(f"Invalid command: {args[0]}")
        return

    for currentFile in currentDirectory.glob("*.py"):
        module = ".".join(currentFile.parts)[:-3]
        name = currentFile.stem
        description = import_module(module).help()

        print(f"{name + ':':<20}{description}")


def help() -> str:
    return "Description of commands."
