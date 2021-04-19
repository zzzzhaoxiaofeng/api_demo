from core.Client import Client
import pytest
import base64
import random
import csv
import time
from core.mailer import send_mail
from core.Dingding import send_dingding
import pymysql

# 存全局变量字典
DATA = {}

# @pytest.fixture()
# def conn_db():
#     connect = pymysql.connect(host="0.0.0.1", port=3306, db="data_name", user="root", password="123456")
#     return connect
#     yield
#     connect.close()


@pytest.fixture()
def client():
    return Client()


# 关联使用的夹具函数
@pytest.fixture()
def set():
    def __set(key,value):
        DATA[key] = value
    return __set

@pytest.fixture()
def get():
    def __get(key):
        return  DATA.get(key)
    return __get


# Utils 工具方法
@pytest.fixture()
def bs64():
    def __bs64(source):
        res = ""
        for i in range(0, 3):
            res = res + str(random.randint(0, 9))
        return base64.b64encode((res + source).encode("utf-8")).decode('utf-8')
    return __bs64


# 参数化
def __csv_reader(filename):
    reslut = []
    with open(file=f"./data/{filename}", mode="r", encoding="utf-8") as f:
        readers = csv.reader(f)
        for content in readers:
            reslut.append(content)
    return reslut[1:]


# 针对login的参数化夹具函数
@pytest.fixture(params=__csv_reader("login.csv"))
def login(request):
    return request.param

# 添加会议接口参数化
@pytest.fixture(params=__csv_reader("add_event.csv"))
def add_event(request):
    return request.param



def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''收集测试结果'''
    # print(terminalreporter.stats)
    # print("total:", terminalreporter._numcollected)
    # print('passed:', len(terminalreporter.stats.get('passed', [])))
    # print('failed:', len(terminalreporter.stats.get('failed', [])))
    # print('error:', len(terminalreporter.stats.get('error', [])))
    # print('skipped:', len(terminalreporter.stats.get('skipped', [])))
    # # terminalreporter._sessionstarttime 会话开始时间
    # duration = time.time() - terminalreporter._sessionstarttime
    # print('total times:', duration, 'seconds')

    # 可以拼接一个大字符串 直接发邮件，可以写一个HTML嵌入数据，直接发邮件
    total = terminalreporter._numcollected
    passed = len(terminalreporter.stats.get('passed', []))
    failed = len(terminalreporter.stats.get('failed', []))
    error = len(terminalreporter.stats.get('error', []))
    skipped = len(terminalreporter.stats.get('skipped', []))
    duration = round(time.time() - terminalreporter._sessionstarttime)

    tmp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    msg_str = f"""\n测试时间：{tmp}
    用例总数：{total}
    成功：{passed}
    失败：{failed}
    错误：{error}
    跳过：{skipped}
    总用时：{duration}s \n"""

    send_dingding(msg="接口测试结果："+msg_str)

    # 发邮件
    # send_mail(receivers=['2511390047@qq.com'],content=str(reslut))






# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     # 获取钩子方法的调用结果，item是测试用例，call是测试步骤
#     out = yield
#     print('用例执行结果', out)
#     #从钩子方法的调用结果中获取测试报告
#     report = out.get_result()
#     print('测试报告：%s' % report)
#     print('步骤：%s' % report.when)
#     print('nodeid：%s' % report.nodeid)
#     print('description:%s' % str(item.function.__doc__))
#     print(('运行结果: %s' % report.outcome))