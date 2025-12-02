from main import is_armstrong


def test_3_digit_armstrong():
    assert is_armstrong(153)
    assert not is_armstrong(123)


def test_4_digit_armstrong():
    assert is_armstrong(9474)
    assert not is_armstrong(9475)


def test_1_digit_armstrong():
    assert is_armstrong(5)
