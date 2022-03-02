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

if len(sys.argv) < 2:
    fatal()

dictionary_link = sys.argv[1]
length = sys.argv[2] if len(sys.argv) > 2 else 5

try_url = False
try:
    with open(dictionary_link) as f:
        dictionary = f.read()
except FileNotFoundError:
    try_url = True

if try_url:
    try:
        resp = urllib.request.urlopen(dictionary_link)
        dictionary = resp.read().decode()
    except Exception:
        fatal()

words = dictionary.split()
