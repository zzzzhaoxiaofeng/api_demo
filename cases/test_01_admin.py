import allure

@allure.epic("用户管理")
@allure.feature("管理员登录接口")
class TestAdmin(object):

    url = "http://123.56.99.53:9000/event/api/admin/"

    @allure.story("正向")
    @allure.title("正向流程")
    @allure.description("管理员正常登录流程")
    def test_admin01(self,client,bs64,set):
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        client.set_body({"username": "admin", "password": bs64("admin")})
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 0)
        set("admin-uid",client.res_json_value("/uid"))
        set("admin-token", client.res_json_value("/token"))


    @allure.story("反向")
    @allure.title("用户名为空")
    @allure.description("登录的用户名为空")
    def test_admin02(self,client):
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        client.set_body({"username": "", "password": "MjM0YWRtaW4="})
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code",10001)


    @allure.story("反向")
    @allure.title("密码错误")
    @allure.description("登录的密码错误")
    def test_admin03(self,client):
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        client.set_body({"username": "admin", "password": "123456"})
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 10000)


    @allure.story("反向")
    @allure.title("非管理员登录")
    @allure.description("无权限普通用户登录")
    def test_admin04(self,client,bs64):
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        client.set_body({"username": "zhaohaha", "password": bs64("123456")})
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 10002)

