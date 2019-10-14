from win32com.client import Dispatch


voice = Dispatch("SAPI.SpVoice")


def run(args: list) -> None:
    args = " ".join(args) if args else "Não digitou nada..."
    voice.speak(args)


def help() -> str: return "Say anything."
