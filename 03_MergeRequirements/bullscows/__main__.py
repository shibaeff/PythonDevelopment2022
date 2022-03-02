from . import gameplay
import sys
import urllib.request

def ask(prompt: str, valid: list[str] = None) -> str:
    if valid is not None:
        guess = input(prompt)
    else:
        while (guess := input(prompt)) not in valid:
            continue
    return guess

def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))