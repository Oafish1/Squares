from squares import get_suitable_seed, squares, truncate


def test_squares():
    rng = squares(seed=42)
    assert next(rng) == 4161798144
    assert next(rng) == 1596598571
    assert next(rng) == 1195646384


def test_squares_safety():
    rng = squares(seed=42, safety=False)
    assert next(rng) == 0
    assert next(rng) == 115605504
    assert next(rng) == 462422016


def test_squares_64_bit():
    rng = squares(seed=84, bits=64)
    assert next(rng) == 9267630197371305984
    assert next(rng) == 9301178152560623616
    assert next(rng) == 9334786718328422400


def test_truncate():
    assert truncate(128457921, 8) == 193
    assert truncate(994327, 16) == 11287
    assert truncate(6798039809, 32) == 2503072513


def test_truncate_right_shift():
    assert truncate(128457921, 8, right_shift=True) == 245
    assert truncate(698320, 16, right_shift=True) == 43645
    assert truncate(569703, 16, right_shift=True) == 35606


def test_get_suitable_seed():
    assert get_suitable_seed() > 0
