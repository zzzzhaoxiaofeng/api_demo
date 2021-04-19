import allure
import pytest

@allure.epic("用户管理")
@allure.feature("用户注册接口")
class Testregister(object):

    url = "http://123.56.99.53:9000/event/api/register/"

    # @allure.story("正向")
    # @allure.title("正常注册流程")
    # @allure.description("正常注册流程")
    # def test_register01(self,client):
    #     client.url  = self.url
    #     client.method = "POST"
    #     client.body_type ="url-encode"
    #     data = {"username": "zhanger", "password": "123456",
    #             "phone": "13024282785", "email": "xiedajiao@163.com"}
    #     client.set_body(data)
    #     client.send()
    #     client.check_res_status_code_is_200()
    #     client.check_res_times_less_than(500)
    #     client.check_json_value_equal("/error_code",0)


    @allure.story("反向")
    @allure.title("手机号错误")
    @allure.description("手机号不符合格式要求")
    def test_register02(self,client):
        client.url  = self.url
        client.method = "POST"
        client.body_type ="url-encode"
        data = {"username": "ouyangnana", "password": "123456",
                "phone": "123456789123456789", "email": "xiaozhao@163.com"}
        client.set_body(data)
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code",10005)

    @allure.story("反向")
    @allure.title("用户名格式错误")
    @allure.description("用户名格式错误，需以字母开头")
    def test_register03(self, client):
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        data = {"username": "123zhangs", "password": "123456",
                "phone": "13866666666", "email": "zhangs@163.com"}
        client.set_body(data)
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 10003)


    @allure.story("反向")
    @allure.title("密码格式错误")
    @allure.description("密码超出长度限制")
    def test_register04(self, client):
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        data = {"username": "lisiyu", "password": "123456789012345",
                "phone": "13866666666", "email": "lisiyu@163.com"}
        client.set_body(data)
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 10004)

    @allure.story("反向")
    @allure.title("邮箱格式无效")
    @allure.description("邮箱格式无效")
    def test_register05(self, client):
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        data = {"username": "guangkun", "password": "123456",
                "phone": "13866666666", "email": "guangkun"}
        client.set_body(data)
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 10006)

    @allure.story("反向")
    @allure.title("用户信息已存在")
    @allure.description("用户信息已存在")
    def test_register06(self, client):
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        data = {"username": "zhaohaha", "password": "123456",
                 "phone":"15088886666","email":"xiaozhao@163.com"}
        client.set_body(data)
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 10007)

    @allure.story("反向")
    @allure.title("用户名为空")
    @allure.description("用户名为空")
    def test_register06(self, client):
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        data = {"username": "", "password": "123456",
                "phone": "15088886666", "email": "xiaozhao@163.com"}
        client.set_body(data)
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 10001)


