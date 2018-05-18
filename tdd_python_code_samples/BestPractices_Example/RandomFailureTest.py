import random

count = 1

def test_failRandomly():
    random.seed()
    assert random.randint(1, 100) % 2 == 0


