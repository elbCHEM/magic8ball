from magic8ball.logic import ANSWERS, get_answer

SAMPLE_SIZE = 1_000_000


def test_output_space() -> None:
    assert not ({get_answer() for _ in range(SAMPLE_SIZE)} ^ set(ANSWERS))
