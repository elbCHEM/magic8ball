import math
from oracle.logic import SECRET_MESSAGES_ODDS, use_secret_message

SAMPLE_SIZE = 1_000_000


def test_probability() -> None:
    n_events = [use_secret_message() for _ in range(SAMPLE_SIZE)].count(True)
    n_min, n_max = interval_of_confidence_3sigma(SAMPLE_SIZE)
    if not (n_min <= n_events <= n_max):
        assert False, f'Measured {n_events}. Expected between {n_min} and {n_max}'


def interval_of_confidence_3sigma(sample_size: int) -> tuple[int, int]:
    """Confidence interval of 3 sigma ~ 99.73"""
    p = 1 / SECRET_MESSAGES_ODDS
    __mean = sample_size * p
    __std = math.sqrt(sample_size * p * (1 - p))
    return math.floor(__mean - 3*__std), math.ceil(__mean + 3*__std)