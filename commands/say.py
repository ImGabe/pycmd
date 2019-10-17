from win32com.client import Dispatch


voice = Dispatch("SAPI.SpVoice")


def run(args: list) -> None:
    args = " ".join(args) if args else "Type something for me to say"
    voice.speak(args)


def help() -> str:
    return "Say anything."
