import pytest


@pytest.fixture(params=[1,2,3,4,5],ids=['num1', 'num2', 'num3', 'num4', 'num5'])
def setUp(request):
    return request.param

class TestDemo02:
    def testadd(self,setUp):
        print('excute TestDemo02 --> testadd')
        assert 2>=setUp