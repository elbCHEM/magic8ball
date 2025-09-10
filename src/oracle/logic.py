import random
from typing import LiteralString

SECRET_MESSAGES_ODDS = 256


ANSWERS: list[LiteralString] = [
    # Positive
    "Yes.",
    "Definitly.",
    "Probaly.",
    "Absolutely.",
    "Nothing have ever been more true.",

    # Negative
    "No.",
    "Definitly not.",
    "Probably not.",
    "Absolutely not.",
    "Under no circumstances.",

    # Neutral
    "I don't know.",
    "That is up to you to decide.",
    "Maybe.",
    "That is very subjective.",
    "It is not certain.",

    # Funny
    "Why are you asking me?",
    "If the stars align, then maybe?",
    "Don't ask me!",
    "You don't you ask your friends? Oh wait! That's right. You don't have any.",
    r"¯\_(ツ)_/¯",
]


SECRET_MESSAGES: list[LiteralString] = [
    "Aww sltw esp xtrsej ajeszy opgpwzapcd!",
    "Hplgj xpelwd cfwpd",
    "Cy-Km-Sl!",
]


def get_answer() -> LiteralString:
    if use_secret_message():
        return random.choice(SECRET_MESSAGES)
    return random.choice(ANSWERS)


def use_secret_message() -> bool:
    """Returns True with odds 1 to 256"""
    return random.randint(1, SECRET_MESSAGES_ODDS) == 1
