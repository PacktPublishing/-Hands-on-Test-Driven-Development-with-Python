from unittest.mock import MagicMock
from my_abc import AbstractAdder, ConcreteAdder, AddExecuter

def test_AddExecuterCallAddAndReturnsResult():
    mock_adder = MagicMock(AbstractAdder)
    mock_adder.add = MagicMock(return_value=3)
    result = AddExecuter(mock_adder)
    mock_adder.add.assert_called_once_with(1, 2)
    assert result == 3
