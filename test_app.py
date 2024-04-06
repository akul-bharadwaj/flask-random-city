from app import random_city


def test_random_city():
    assert "Bengaluru" or "Liverpool" or "Kuala Lumpur" in random_city()
