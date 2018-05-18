import TestVariables

def test_one():
    TestVariables.test_value = 1
    assert True

def test_two():
    assert TestVariables.test_value == 1

