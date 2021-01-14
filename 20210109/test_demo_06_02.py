# pyrest执行顺序：包/文件-->根据ASCII码升序执行
# 文件内部的测试方法-->哪个方法写在前面就先执行
import pytest
class TestDemo01:
    @pytest.mark.run(order=5)
    def testadd03(self):
        print( 'excec TestDemo0602 -- > testadd03')
        assert 1+1 == 2
    @pytest.mark.run(order=6)
    def testadd04(self):
        print( 'excec TestDemo0602 -- > testadd04')
        assert 1+1 == 2

    # @pytest.mark.last   # 最后执行
    @pytest.mark.run(order=7)
    def testadd01(self):
        print( 'excec TestDemo0602 -- > testadd01')
        assert 1+1 == 2
    @pytest.mark.run(order=8)
    def testadd02(self):
        print( 'excec TestDemo0602 -- > testadd02')
        assert 1+1 == 2
