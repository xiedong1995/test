import unittest
from time import strftime
from HTMLTestRunner import HTMLTestRunner

import yagmail


# 定义测试用例的目录为当前目录下的test_case目录

def send_mail(report):
    yag = yagmail.SMTP(user = "albinocary@163.com",
                       password='xd123456',
                       host = 'smtp.163.com')
    subject = '主题,自动化测试报告'
    contents = '正文,请查看附件'
    yag.send('1015560101@qq.com',subject,contents,report)
    print('emaile has send out!')



test_dir = "."
suit = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == "__main__":
    # 获取当前时间
    now_time = strftime("%Y-%m-%d %H_%M_%S")
    html_report = './test_report/'+now_time+'result.html'
    fp = open(html_report, 'wb')
    runner = HTMLTestRunner(stream=fp, title="百度搜索测试报告",
                            description="运行环境：Windows 10，chrome 浏览器")
    runner.run(suit)
    fp.close()
    send_mail(html_report)
