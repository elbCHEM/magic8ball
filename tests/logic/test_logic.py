from oracle.logic import ANSWERS, SECRET_MESSAGES, get_answer

SAMPLE_SIZE = 100_000


def test_normal_messages(monkeypatch) -> None:
    monkeypatch.setattr('oracle.logic.use_secret_message', always_false)
    assert not ({get_answer() for _ in range(SAMPLE_SIZE)} ^ set(ANSWERS))


def test_secret_messages(monkeypatch) -> None:
    monkeypatch.setattr('oracle.logic.use_secret_message', always_true)
    assert not ({get_answer() for _ in range(SAMPLE_SIZE)} ^ set(SECRET_MESSAGES))


def test_output_space() -> None:
    output_space = set(ANSWERS) | set(SECRET_MESSAGES)
    assert not ({get_answer() for _ in range(SAMPLE_SIZE)} ^ output_space)


def always_false(*_, **__):
    return False


def always_true(*_, **__):
    return True