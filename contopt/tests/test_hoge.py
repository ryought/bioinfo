import pytest

@pytest.fixture
def variable():
    x = 'example message'
    return x

def test_hoge():
    assert 1 == 1

@pytest.mark.xfail
def test_i_will_fail():
    assert 1 == 0

def test_aaa(variable):
    print(variable)
    assert variable == 'example message'
