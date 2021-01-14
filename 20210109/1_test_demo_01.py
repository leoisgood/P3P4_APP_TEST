import pytest

@pytest.fixture(autouse=True)
def setUp():
    print('start test')
    yield
    print('test end')

class TestDemo01:
    def testadd(self):
        print( 'excec TestDemo01 -- > testadd')
        assert 1+1 == 2
    def testsub(self):
        print()
        assert 1-1 == 0