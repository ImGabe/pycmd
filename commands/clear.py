from os import system, name


def run(args: list) -> None:
    system("cls") if name == "nt" else system("clear")


def help() -> str:
    return "Clear console."
