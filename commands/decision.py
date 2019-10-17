import requests


def run(args: list) -> None:
    r = requests.get('https://yesno.wtf/api')
    input("Ask your question:\n")
    print(f"The answer is {r.json()['answer']}.")


def help() -> str:
    return "Let luck decide for you on yes or no questions."
