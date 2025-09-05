import re
import pytest
from magic8ball.flow import PROPER_EXIT_STRING, main



@pytest.mark.parametrize('quitstring', ['', ' ', 'quit', 'QUIT', 'QuIt'])
def test_quitting_program(monkeypatch, quitstring: str) -> None:
    last_string_printed = None
    def savelastprint(string: str, **__) -> None:
        nonlocal last_string_printed
        last_string_printed = string
    monkeypatch.setattr('builtins.print', savelastprint)

    def mockinput(*_, **__) -> str:
        return quitstring
    monkeypatch.setattr('builtins.input', mockinput)

    main()
    assert last_string_printed == PROPER_EXIT_STRING
