import pytest

class TestDemo0501:
    @pytest.mark.smoketest
    @pytest.mark.systest
    def test_add_01(self):
        print('exec TestDeom0501-->test_add_01')
        assert 1+3==4
    @pytest.mark.systest
    def test_add_02(self):
        print('exec TestDeom0501-->test_add_02')
        assert 1+3==4