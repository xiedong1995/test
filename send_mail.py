import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

import yagmail


def send_mail1():
    """发送不带附件的邮件"""
    subject = "这是邮件标题"

    # 编写HTML类型的邮件正文
    msg = MIMEText('<html><h1>你好!</h1></html>', 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    # 发邮件
    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")  # 邮箱的smtp服务器
    smtp.login("albinocary@163.com", "xd123456")  # 登录,用户名,授权码
    smtp.sendmail("albinocary@163.com", "1015560101@qq.com", msg.as_string())  # 发件人,收件人,内容
    smtp.quit()  # 退出


def send_mail2():
    """发送带附件的邮件"""
    subject = "这是一封带附件的邮件"
    with open('log.txt', 'rb') as f:
        send_att = f.read()

    att = MIMEText(send_att, 'text', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="log.txt"'
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg.attach(att)

    # 发邮件
    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")  # 邮箱的smtp服务器
    smtp.login("albinocary@163.com", "xd123456")  # 登录,用户名,授权码
    smtp.sendmail("albinocary@163.com", "albinocary@163.com", msg.as_string())  # 发件人,收件人,内容
    smtp.quit()  # 退出


def send_mail_for_yagmail():
    # 链接邮箱服务器
    yag = yagmail.SMTP(user="albinocary@163.com", password="xd123456", host="smtp.163.com")
    contents = ['这是邮件正文', '这是邮件第二正文']
    # 发送邮件
    yag.send('1015560101@qq.com', '邮件标题', contents)
    # 发送给多人
    # yag.send(['aa@163.com','bb@qq.com','cc@gmail.com'],'邮件标题','正文')

    # 发送带附件的邮件
    # yag.send('aa@163.com','标题','正文',['文件1路径','文件二路径'])


if __name__ == '__main__':
    # send_mail2()
    send_mail_for_yagmail()
