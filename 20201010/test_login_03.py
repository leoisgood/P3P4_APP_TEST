import pytest
import allure
import os
@pytest.fixture(name='set')
def set_up():
    print('前置条件:***')
    yield
    print('后置处理:***')

@allure.step('步骤一：调用首页接口获取token')
def step_01():
    pass
@allure.step('步骤二：调用登录接口')
def step_02():
    pass

@allure.epic('[epic]italki_学生管理系统')
@allure.feature('[feature]italki_学生管理系统V1.0')
class TestLogin03:
    @allure.story('[story]登录模块')
    @allure.title('[title]case01 验证正确的用户名和密码能否成功登录')
    def test_login_success(self):
        step_01()
        step_02()
        with allure.step('步骤三：验证判断'):
            pass
        with allure.step('步骤四：验证判断'):
            pass
        with open(os.path.join(os.path.dirname(__file__), 'images', 'demo.jpeg'), 'rb') as img_file:
            img_obj = img_file.read()
            allure.attach(img_obj,'error screenshot', allure.attachment_type.JPG)
        assert True

    @allure.story('[story]登录模块')
    @allure.title('[title]case02 验证正确的用户名和密码登录是否失败')
    def test_login_fail(self):
        assert True
