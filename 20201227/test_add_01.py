import pytest

# class Testadd01:
#    def test_add_case_01(self):
#        assert 1+1 == 5

#  只写测试方法
def test_add_case_01():
    assert 1 + 1 == 5

if __name__ == '__main__':
    pytest.main()