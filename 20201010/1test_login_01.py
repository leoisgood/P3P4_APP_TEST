import pytest
import allure

@allure.epic('[epic]italki_学生管理系统')
@allure.feature('[feature]italki_学生管理系统V1.0')
class TestLogin01:
    @allure.story('[story]登录模块')
    @allure.title('[title]case01 验证正确的用户名和密码能否成功登录')
    def test_login_success(self):
        assert True

    @allure.story('[story]登录模块')
    @allure.title('[title]case02 验证正确的用户名和密码登录是否失败')
    def test_login_fail(self):
        assert True
