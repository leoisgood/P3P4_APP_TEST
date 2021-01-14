import pytest
class TestDemo01:
    def testadd(self,main_package,test_package_01):
        print( 'excec TestDemo01 -- > testadd')
        assert 1+1 == 2
    def testsub(self):
        print()
        assert 1-1 == 1