from dingtalkchatbot.chatbot import DingtalkChatbot


def send_dingding(msg):
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=ce39d35baa0b59652d29ccf9ef8c3a0460d5aa706f462911be4223be18dd1077"
    # 初始化机器人小丁
    xiaoding = DingtalkChatbot(webhook)
    # Text消息@所有人
    # at_mobiles = ['15011295082']
    try:
        xiaoding.send_text(msg=msg, is_at_all=True)
        print("钉钉发送成功")
    except Exception as e:
        print("钉钉发送失败！",e)





# 定制发送的内容：markdown
#
# xiaoding.send_markdown(title='接口自动化巡查结果', text='#### 测试开始时间：2020-07-01 13：15\n'
#                            '用例总数： 74\n'
#                            '成功： 68\n'
#                            '失败： 6\n',
#                            message_url='http://www.kwongwah.com.my/?p=454748",
#                            is_at_all=True)