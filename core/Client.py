import requests
import jsonpath
import allure
import json

class BodyType(object):
    URL_ENCODE = 'url-encode'
    JSON = 'json'
    XML = 'xml'
    FILES = 'form-data'

class Method(object):
    GET='GET'
    POST='POST'


class Client(object):

    def __init__(self):
        self.url = None
        self.method = Method.GET
        self.params = {}
        self.headers = {}
        self.body_type = None
        self.data = {}
        self.res = None
        self.timeout = 10
        self.flag = 0


    def set_header(self,key,value):
        self.headers[key] = value


    def set_headers(self,header_dict):
        if isinstance(header_dict,dict):
            self.headers.update(header_dict)
        else:
            raise Exception("头信息格式错误，请使用字典形式")

    def set_cookies(self,cookie_dict):
        if isinstance(cookie_dict,dict):
            list = []
            for key ,value in cookie_dict.items():
                list.append(f"{key}={value}")
                cookie_str = ";".join(list)
            if "Cookie" in self.headers.keys():
                self.headers["Cookie"] += cookie_str
            else:
                self.headers["Cookie"] = cookie_str
        else:
            raise Exception("响应结果为空")

    def set_body(self,body_dict):
        if isinstance(body_dict,dict):
            self.data = body_dict
        else:
            raise Exception("正文体格式错误，请使用字典形式")

    @allure.step("接口请求的详细信息")
    def send(self):

        if self.method == Method.GET:
            self.res = requests.get(url=self.url,params=self.params,headers=self.headers,timeout=self.timeout)
            self.__request_info()

        elif self.method == Method.POST:
            if self.body_type == None:
                self.__request_info()
                self.res = requests.post(url=self.url,headers=self.headers,timeout=self.timeout)

            elif self.body_type == BodyType.URL_ENCODE:
                self.set_header("Cont-Type","application/x-www-form-urlencoded")
                self.__request_info()
                self.res = requests.post(url=self.url, headers=self.headers, data=self.data, timeout=self.timeout)

            elif self.body_type == BodyType.JSON:
                self.set_header("Content-Type","application/json")
                self.__request_info()
                self.res = requests.post(url=self.url, headers=self.headers, json=self.data, timeout=self.timeout)


            elif self.body_type == BodyType.XML:
                self.set_header('Content-Type','text/xml')
                self.res = requests.post(url=self.url, headers=self.headers, data =self.data.get('xml'), timeout=self.timeout)
                self.__request_info()

            elif self.body_type == BodyType.FILES:
                self.__request_info()
                self.res = requests.post(url=self.url, headers=self.headers, files=self.data,
                                         timeout=self.timeout)
            else:
                raise Exception("POST请求无效")
        else:
            raise Exception("无效的请求方法类型：只支持GET和POST请求")

        self.__res_info()

    # allure 附件形式在报告中展示详细信息
    @allure.step("请求详细信息")
    def __request_info(self):
        # 在allure报告中打印接口的详细的内容
        allure.attach(self.url, "请求地址", allure.attachment_type.TEXT)
        allure.attach(self.method, "请求方法", allure.attachment_type.TEXT)
        allure.attach(json.dumps(self.headers), "请求头", allure.attachment_type.TEXT)
        allure.attach(json.dumps(self.data), "请求正文", allure.attachment_type.TEXT)


    @allure.step("响应的详细信息")
    def __res_info(self):
        allure.attach(str(self.get_status_code), "响应状态码", allure.attachment_type.TEXT)
        allure.attach(str(self.get_response_times), "响应时间", allure.attachment_type.TEXT)
        allure.attach(str(self.get_text), "响应正文", allure.attachment_type.TEXT)


    @property
    def get_text(self):
        if self.res is not None:
            return self.res.text
        else:
            raise Exception("接口响应为空")

    @property
    def get_status_code(self):
        if self.res is not None:
            return self.res.status_code
        else:
            raise Exception("接口的响应状态码为空")

    @property
    def get_response_times(self):
        if self.res is not None:
            return round(self.res.elapsed.total_seconds()*1000)
        else:
            raise Exception("响应结果为空，无法获取响应时间")

    # 根据path直接取值，返回值  ，也可以返回列表，为空时返回空列表
    def res_json_value(self,path):
        if self.res is not None:
            path = path.replace("/",".")
            reslut = jsonpath.jsonpath(self.res.json(),"$"+path)
            if reslut:
                return reslut[0]
            else:
                return None
        else:
            raise Exception("响应结果为空，无法通过path取值")

    #根据json的key 取value
    def get_json_value_by_key(self,key):
        if self.res is not None:
            value = self.res.json().get(key)
            if value:
                return value
            else:
                return None
        else:
            raise ("响应结果为空，无法通过key值取value")


    # 断言
    # 失败退出断言
    # @allure.step("响应断言信息")
    # def check_json_value_equal(self, path, exp, msg=None):
    #     act = self.res_json_value(path)
    #     assert act == exp, msg
    #     message = f"检查点【json值等于】，执行成功。预期结果为{act}，实际结果为：{exp}"
    #     allure.attach(message, "json值检查点Pass", allure.attachment_type.TEXT)

    # 失败不退出的断言
    @allure.step("响应断言信息")
    def check_json_value_equal(self,path,exp,msg=None):
        act = self.res_json_value(path)
        try:
            assert act == exp,msg
            message = f"检查点【json值等于】，执行成功。预期结果为{act}，实际结果为：{exp}"
            allure.attach(message, "json值检查点Pass", allure.attachment_type.TEXT)
        except:
            self.flag +=1
            message = f"断言失败，预期结果为{exp}，实际结果为：{act}"
            allure.attach(message, "json值检查点Failure", allure.attachment_type.TEXT)

    @allure.step("响应时间检查")
    def check_res_status_code_is_200(self):
        try:
            assert self.get_status_code == 200
            message = f"检查点【响应状态码】，执行成功。预期结果为：200，实际结果为：{self.get_status_code}"
            allure.attach(message, "json值检查点Pass", allure.attachment_type.TEXT)

        except:
            self.flag +=1
            message = f"断言失败，预期结果为[200]，实际结果为：{self.get_status_code}"
            allure.attach(message, "json值检查点Failure", allure.attachment_type.TEXT)

    # 检查点 包含关键字信息
    def check_res_contains(self, exp,msg=None):
        assert exp in self.get_text,msg
        message = f"检查点【响应报文包含关键字】，执行成功。预期结果为：{exp}，实际结果为：{self.get_text}"
        allure.attach(message, "json值检查点Pass", allure.attachment_type.TEXT)

    # 响应时间低于500ms
    def check_res_times_less_than(self,exptimes,msg=None):
        assert self.get_response_times < exptimes
        message = f"检查点【响应时间小于】，执行成功，预期结果为：{exptimes}ms，实际结果为：{self.get_response_times}ms"
        allure.attach(message, "json值检查点Failure", allure.attachment_type.TEXT)

    # 数据库检查点
    def check_db(self, conn_db,sql, exp, index=0):
        cursor = conn_db.cursor()
        cursor.execute(sql)
        reslut = cursor.fetchall()[index]  # 返回元组,查出多组数据时，加索引查要第几个
        assert reslut == exp, "数据库检查错误：实际结果{act},预期结果{exp}".format(act=reslut[0], exp=exp)  # exp 也是元组


    # 检查断言的最终结果，如果flag大于0 ，测试用例失败
    def check_reslut(self):
        if self.flag > 0:
            assert False

