import pytest

greetings = [
    ("Good", "Morning", "Good Morning"),
    ("Good", "Afternoon", "Good Afternoon"),
    ("Good", "Evening", "Good Evening"),
    ("Good", "Night", "Good Night"),
]

@pytest.mark.parametrize('a, b, expected', greetings)
def test_param(a, b, expected):
    result = a + " " + b
    assert result == expected
