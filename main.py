from importlib import import_module
from pathlib import Path
from sys import exit


currentDirectory = Path("commands")


def run(filename: str, args: list) -> None:
    try:
        for currentFile in currentDirectory.glob(f"{filename}.py"):
            module = ".".join(currentFile.parts)[:-3]
            import_module(module).run(args)
    except OSError:
        pass


while True:
    try:
        line = input(f"> ").strip().split(" ")
        command = line[0]
        args = line[1:] if len(line) > 1 else None
        run(command, args)
    except KeyboardInterrupt:
        exit()
