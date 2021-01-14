import pytest
import allure

@allure.epic('[epic]italki_学生管理系统')
@allure.feature('[feature]italki_学生管理系统V1.0')
class TestStuManage02:
    @allure.story('[story]学生新增')
    @allure.title('[title]case01 验证添加学生信息成功')
    def test_add_stu_info_01(self):
        assert True

    @allure.story('[story]学生修改')
    @allure.title('[title]case02 验证添加修改信息成功')
    def test_add_stu_info_02(self):
        assert True