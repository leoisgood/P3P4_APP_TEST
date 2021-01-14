import pytest

@pytest.fixture()
def setUp():
    print('初始化')
    yield
    print('测试环境清理')

def test_case_01(setUp):
    print('执行test_case_01')
    assert True


def test_case_02():     # setUp可以选择噢诶之
    print('执行test_case_02')
    assert True

if __name__ == '__main__':
    pytest.main(["-s"])  # -s 显示print信息
