import random
from typing import LiteralString


ANSWERS: list[LiteralString] = [
    # Positive (5/20)
    "Yes.",
    "Definitly.",
    "Probaly.",
    "Absolutely.",
    "Nothing have ever been more true.",

    # Negative (5/20) (v)
    "No.",
    "Definitly not.",
    "Probably not.",
    "Absolutely not.",
    "Under no circumstances.",

    # Neutral (5 / 20) (v)
    "I don't know.",
    "That is up to you to decide.",
    "Maybe.",
    "That is very subjective.",
    "It is not certain.",

    # Funny (5 / 20)
    "Why are you asking me?",
    "If the stars align, then maybe?",
    "Don't ask me!",
    "You don't you ask your friends? Oh wait! That's right. You don't have any.",
    r"¯\_(ツ)_/¯",
]


def get_answer() -> LiteralString:
    return random.choice(ANSWERS)
