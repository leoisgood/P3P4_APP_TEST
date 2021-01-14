import pytest

# pytest参数化
@pytest.fixture(params=[(1,1,2),(3,9,12),(7,8,15)], ids=['add01','add02','add03'])
def setUp(request):
    return request.param


class TestDemo03:
    def testadd(self,setUp):
        print('excute TestDemo03-->testadd')
        assert setUp[0]+setUp[1]==setUp[2]

