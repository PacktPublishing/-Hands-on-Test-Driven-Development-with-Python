
import pytest
from unittest.mock import MagicMock
from Checkout import Checkout

lineCnt = 0

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    return checkout

def test_canCalculateTotal(checkout):
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1

def test_getCorrectTotalWithMultipleItems(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3

def test_canAddDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)

def test_canApplyDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.calculateTotal() == 2

def test_exceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem("c")

def test_verifyReadPricesFile(checkout, monkeypatch):
    mock_file = MagicMock()
    mock_file.__enter__.return_value.__iter__.return_value = ["c 3"]
    mock_open = MagicMock(return_value = mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    checkout.readPricesFile("testfile")
    checkout.addItem("c")
    result = checkout.calculateTotal()
    mock_open.assert_called_once_with("testfile")
    assert result == 3

