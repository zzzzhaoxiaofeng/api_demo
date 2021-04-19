import allure


@allure.epic("活动管理")
@allure.feature("添加活动接口")
class Testadd_event(object):

    url = "http://123.56.99.53:9000/event/api/add_event/"
    @allure.story("正向")
    @allure.title("添加活动正向流程")
    @allure.description("正常添加一个会议")
    def test_add_event01(self,client,get,set):
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        client.set_headers({"uid": get("admin-uid"), "key": get("admin-token")})
        client.set_body({"title":"华为新品发布会1111", "limit":500, "status":0, "address":"北京国家会议中心",
                         "time":"2021-05-01 08:00:00", "price":100, "type":"创业"})
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 0)
    #    设置一个全局变量"event_id"
        set("event_id",client.res_json_value("/data/event_id"))

    @allure.story("反向")
    @allure.title("活动标题超长")
    @allure.description("活动标题超限制长度，限制20")
    def test_add_event02(self,client,get):
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        client.set_headers({"uid": get("admin-uid"), "key": get("admin-token")})
        client.set_body({"title":"华为新品发布会华为新品发布会华为新品发布会华为新品发布会华为新品发布会华为新品发布会华为新品发华为新品发布会布会华为新品发布会",
                         "limit":500, "status":0, "address":"北京国家会议中心",
                         "time":"2021-12-31 08:00:00", "price":100, "type":"创业"})
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 10011)

    @allure.story("反向")
    @allure.title("活动状态不存在")
    @allure.description("活动状态，未开始:0(默认)；进行中:1；已结束:2")
    def test_add_event03(self,client,get):
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        client.set_headers({"uid": get("admin-uid"), "key": get("admin-token")})
        client.set_body({"title": "华为新品发布会002", "limit": 500, "status": 3, "address": "北京国家会议中心",
                         "time": "2021-12-31 08:00:00", "price": 100, "type": "创业"})
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 10012)

    @allure.story("反向")
    @allure.title("活动日期格式错误")
    @allure.description("活动日期格式错误，建议格式：2020-05-01 ")
    def test_add_event04(self,client,get):
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        client.set_headers({"uid": get("admin-uid"), "key": get("admin-token")})
        client.set_body({"title": "华为新品发布会003", "limit": 500, "status": 1, "address": "北京国家会议中心",
                         "time": "2000-12-31", "price": 100, "type": "创业"})
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 10013)

    @allure.story("反向")
    @allure.title("活动日期无效")
    @allure.description("活动日期必须大于当前时间24h")
    def test_add_event05(self, client,get):
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        client.set_headers({"uid": get("admin-uid"), "key": get("admin-token")})
        client.set_body({"title": "华为新品发布会004", "limit": 500, "status": 1, "address": "北京国家会议中心",
                         "time": "2009-12-31 08:00:00", "price": 100, "type": "创业"})
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 10014)

    @allure.story("反向")
    @allure.title("活动重复")
    @allure.description("添加已有活动")
    def test_add_event06(self, client,get):
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        client.set_headers({"uid": get("admin-uid"), "key": get("admin-token")})
        client.set_body({"title": "华为新品发布会", "limit": 500, "status": 0, "address": "北京国家会议中心",
                         "time": "2021-12-31 08:00:00", "price": 100, "type": "创业"})
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 10010)

    @allure.story("反向")
    @allure.title("活动类型不存在")
    @allure.description("活动类型不存在，存在有：户外、文娱、亲子、互联网技术、创业")
    def test_add_event07(self, client,get):
        client.url = self.url
        client.method = "POST"
        client.body_type = "url-encode"
        client.set_headers({"uid": get("admin-uid"), "key": get("admin-token")})
        client.set_body({"title": "华为新品发布会hhhh", "limit": 500, "status": 0, "address": "北京国家会议中心",
                         "time": "2021-12-31 08:00:00", "price": 100, "type": "哈哈"})
        client.send()
        client.check_res_status_code_is_200()
        client.check_res_times_less_than(500)
        client.check_json_value_equal("/error_code", 10015)

