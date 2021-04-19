import allure


@allure.epic("活动管理")
@allure.feature("获取活动详情接口")
class Testget_eventdetail(object):

    url ="http://123.56.99.53:9000/event/api/get_eventdetail/"
    @allure.story("正向")
    @allure.title("管理员-正常查询活动详情")
    @allure.description("管理员-正常查询活动详情")
    def test_get_eventdetail01(self,client,get):
        client.url = self.url
        client.method = "GET"
        client.set_headers({"uid": get("admin-uid"), "key": get("admin-token")})
        client.params = {"id":get("event_id")}
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code",0)

    @allure.story("正向")
    @allure.title("普通用户-正常查询活动详情")
    @allure.description("普通用户-正常查询活动详情")
    def test_get_eventdetail02(self,client,get):
        client.url = self.url
        client.method = "GET"
        client.set_headers({"uid": get("login-uid"), "key": get("login-token")})
        client.params = {"id": get("event_id")}
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 0)

    @allure.story("反向")
    @allure.title("活动id不存在")
    @allure.description("查询活动id不存在")
    def test_get_eventdetail03(self, client, get):
        client.url = self.url
        client.method = "GET"
        client.set_headers({"uid": get("login-uid"), "key": get("login-token")})
        client.params = {"id": 0}
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 10017)

