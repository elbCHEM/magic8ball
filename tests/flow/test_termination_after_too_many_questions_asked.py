import pytest
from magic8ball.flow import MAX_QUESTIONS, TooManyQuestionAsked, app_flow


def test_run(monkeypatch) -> None:
    def mockinput(*_, **__) -> str:
        return "Am I correct?"
    monkeypatch.setattr('builtins.input', mockinput)

    def silentprint(*_, **__) -> None:
        pass
    monkeypatch.setattr('builtins.print', silentprint)

    with pytest.raises(TooManyQuestionAsked) as error:
        app_flow()
    assert error.value.questions_asked == MAX_QUESTIONS
