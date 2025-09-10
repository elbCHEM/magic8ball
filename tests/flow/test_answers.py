import re
import pytest
from oracle.logic import ANSWERS
from oracle.flow import TooManyQuestionAsked, app_flow


RESPONCE_PATTERN = re.compile(r"The answer to your question is: \"(.+)\"")


class InvalidAnswer(Exception):
    pass


def test_answers_are_valid(monkeypatch) -> None:
    """Test if the answers provided by oracle matches the correct pattern and if the answer fits"""
    def mockinput(*_, **__) -> str:
        return "Am I correct?"
    monkeypatch.setattr('builtins.input', mockinput)

    def validate_responce(string: str, **__) -> None:
        """Matches string to expected responce pattern and checks answer agains possible answers"""
        if not (__match := RESPONCE_PATTERN.match(string)):
            return
        if (__answer := __match.group(1)) not in ANSWERS:
            raise InvalidAnswer(f'Provided answer "{__answer}" is invalid')
    monkeypatch.setattr('builtins.print', validate_responce)

    monkeypatch.setattr('oracle.logic.use_secret_message', always_false)
    with pytest.raises(TooManyQuestionAsked):
        app_flow()


def always_false(*_, **__):
    return False
