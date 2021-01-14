import pytest

@pytest.fixture(scope='package',name = "setUp1") # 指定运行的名称
def setUp():
    print('测试初始化')
    yield
    print('测试环境清理')

def test_case_01(setUp1):
    print('do test_case_01')
    assert True
def test_case_02(setUp1):    #可选择是否添加setup
    print('do test_case_02')
    assert True

if __name__ == '__main__':
    pytest.main(["-s"]) #-s显示