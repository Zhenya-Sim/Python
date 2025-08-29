import pytest
from String_processor import StringProcessor


@pytest.mark.parametrize("input_text, expected_output", [
    ("train", "Train."),
    ("Python", "Python."),
    ("hard.", "Hard.")
    ])
def test_process_positive(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output


@pytest.mark.parametrize("input_text, expected_output", [
    (" _ ", " _ ."),
    ("", ".")
    ])
def test_process_negative(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output
