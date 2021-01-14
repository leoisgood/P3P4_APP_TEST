import pytest

class TestDemo0502:
    def test_add_01(self):
        print('exec TestDeom0502-->test_add_01')
        assert 1+3==4
    @pytest.mark.smoketest
    def test_add_02(self):
        print('exec TestDeom0502-->test_add_02')
        assert 1+3==4