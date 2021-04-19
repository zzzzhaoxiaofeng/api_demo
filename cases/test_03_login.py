import allure


@allure.epic("用户管理")
@allure.feature("用户登录接口")
class TestLogin(object):

    url = "http://123.56.99.53:9000/event/api/login/"

    @allure.story("正向")
    @allure.title("正常流程")
    @allure.description("用户端用户登录流程")
    def test_login01(self,client,bs64,set):
        client.url = self.url
        client.method = "POST"
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        data = {"username": "zhaohaha", "password": bs64("123456")}
        client.set_body(data)
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 0)
        set("login-uid", client.res_json_value("/uid"))
        set("login-token", client.res_json_value("/token"))


    @allure.story("反向")
    @allure.title("用户名为空")
    @allure.description("登录用户名为空")
    def test_login02(self, client,bs64):
        client.url = self.url
        client.method = "POST"
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        data = {"username": "", "password": bs64("123456")}
        client.set_body(data)
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 10001)


    @allure.story("反向")
    @allure.title("密码为空")
    @allure.description("登录密码为空")
    def test_login03(self, client):
        client.url = self.url
        client.method = "POST"
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        data = {"username": "ouyangnana", "password": ""}
        client.set_body(data)
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 10001)

    @allure.story("反向")
    @allure.title("密码错误")
    @allure.description("登录密码为空")
    def test_login03(self, client, bs64):
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        data = {"username": "zhaohaha", "password": "aa123456"}
        client.set_body(data)
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 10000)


