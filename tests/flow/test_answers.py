import re
import pytest
from magic8ball.logic import ANSWERS
from magic8ball.flow import TooManyQuestionAsked, app_flow


RESPONCE_PATTERN = re.compile(r".*\"(.+)\".*")


class InvalidAnswer(Exception):
    pass


def test_answers_are_valid(monkeypatch) -> None:
    def mockinput(*_, **__) -> str:
        return "Am I correct?"
    monkeypatch.setattr('builtins.input', mockinput)

    def validate_responce(string: str, **__) -> None:
        if not (__match := RESPONCE_PATTERN.match(string)):
            return
        if (__answer := __match.group(1)) not in ANSWERS:
            raise InvalidAnswer(f'Provided answer "{__answer}" is invalid')
    monkeypatch.setattr('builtins.print', validate_responce)

    with pytest.raises(TooManyQuestionAsked):
        app_flow()
