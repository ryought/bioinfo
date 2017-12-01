import pytest
from . import itemset

@pytest.fixture
def variable():
    x = 'example message'
    return x

def test_compute():
    assert 1 == 1

def test_aaa(variable):
    print(variable)
    assert variable == 'example message'
