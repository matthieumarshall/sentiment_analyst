import pytest
from main import elevate_do, elevate_produce


def test_main():
    assert elevate_do() == 5


def test_produce():
    assert elevate_produce() == 1
