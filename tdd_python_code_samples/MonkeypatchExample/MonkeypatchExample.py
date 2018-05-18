import pytest
from unittest.mock import Mock
from unittest.mock import patch
from datetime import datetime

def getDateFromFile(filename):
    infile = open(filename, "r")
    line = infile.readline().strip()
    print("Line: {}".format(line))
    theDate = datetime.strptime(line, "%b %d %Y")
    print("Date: {}".format(theDate))

class ImportantClass:
    def getValue(self):
        return 1

def useImportantClass( theImportantClass ):
    print("{}".format(theImportantClass.getValue()))

# Dummy test
def test_UseImportantClass():
    class MyTestImportantClass:
        def getValue(self):
            return 2

    testClass = MyTestImportantClass()
    useImportantClass(testClass)

def test_MagicMock():
    testClass = ImportantClass()
    testClass.getValue = Mock(spec=testClass.getValue)
    testClass.getValue.return_value = 3
    result = testClass.getValue()
    assert result == 3
    testClass.getValue.assert_called_once()

def functionToPatch():
    print("blah")

def patchedFunction():
    print("bar")

@patch("MonkeypatchExample.functionToPatch", patchedFunction)
def test_patch():
    functionToPatch()

def test_monkeyPatch(monkeypatch):
    monkeypatch.setattr("MonkeypatchExample.functionToPatch", patchedFunction)
    functionToPatch()

def test_wraps(monkeypatch):
    testObj = Mock(spec=functionToPatch, wraps=functionToPatch)
    monkeypatch.setattr("MonkeypatchExample.functionToPatch", testObj)
    functionToPatch()
    testObj.assert_called_once()

if __name__ == "__main__":
    getDateFromFile("test_file.txt")

