import pytest

def fizzBuzz(value):
    return "1"

def test_canCallFizzBuzz():
    fizzBuzz(1)

def test_get1With1PassedIn():
    retVal = fizzBuzz(1)
    assert retVal == "1"