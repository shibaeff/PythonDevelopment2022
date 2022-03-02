import textdistance as td
import random


def bullscows(guess: str, secret: str) -> (int, int):
    bulls = td.hamming.similarity(guess, secret)
    cows = td.bag.similarity(guess, secret)
    return (bulls, cows)