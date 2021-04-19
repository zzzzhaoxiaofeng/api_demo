import requests
import pytest
import allure

@allure.epic("活动管理")
@allure.feature("获取活动列表接口")
class Testget_eventlist(object):


    url = "http://123.56.99.53:9000/event/api/get_eventlist/"


    @allure.title("获取户外活动的活动列表")
    @allure.description("获取类型是【户外活动】的活动列表")
    def test_get_eventlist01(self,client,get):
        client.url = self.url
        client.method = "GET"
        client.set_headers({"uid": get("admin-uid"), "key": get("admin-token")})
        client.params={"type":"户外"}
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_res_contains('"type": "户外"')




    @allure.title("管理员查询活动列表")
    @allure.description("管理员权限获取全部活动列表")
    def test_get_eventlist02(self,client,get):
        client.url = self.url
        client.method = "GET"
        client.set_headers({"uid": get("admin-uid"), "key": get("admin-token")})
        client.send()
        print(client.get_text)
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_res_contains("count")


    @allure.title("普通用户查询活动列表")
    @allure.description("普通用户权限获取类型【创业】活动列表")
    def test_get_eventlist02(self, client, get):
        client.url = self.url
        client.method = "GET"
        client.set_headers({"uid": get("login-uid"), "key": get("login-token")})
        client.params = {"type":"创业"}
        client.send()
        print(client.get_text)
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_res_contains('"type": "创业"')


