from users.models import EmailVerifyCode
from random import choice
import smtplib
from email.header import Header
from email.mime.text import MIMEText
smtp_server='smtp.qq.com'
smtp_port=587
server=smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.set_debuglevel(1)
server.login('1904258580@qq.com','tqgdnhuwkimocdei')
def get_random_code(code_length):
    code_source='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code=''
    for i in range(code_length):
        #随机选择一个字符
        #code+字符
        code+=choice(code_source)
    return code



def sent_email_code(email,send_type):
    #第一步，创建邮箱验证码对象，保存数据库，用来以后做对比
    a=EmailVerifyCode()
    a.email=email
    a.send_type=send_type
    a.code=get_random_code(5)
    a.save()
    #第二步，正式的发邮件功能
    send_title=''
    send_body=''
    if send_type==1:
        send_title='欢迎注册教育网站；'
        send_body=send_title+'请点击以下链接进行激活您的账号；\n http://127.0.0.1:8000/users/user_active/'+a.code
        msg = MIMEText(send_body, 'plain', 'utf-8')
        msg['From'] = '1904258580@qq.com <1904258580@qq.com>'
        msg['Subject'] = Header(u'text', 'utf8').encode()
        msg['To'] = email
        server.sendmail('1904258580@qq.com', [email], msg.as_string())
        server.quit()
    if send_type==2:
        send_title = '重置密码'
        send_body = send_title + '请点击以下链接进行重置您的账号；\n http://127.0.0.1:8000/users/user_reset/' + a.code
        msg = MIMEText(send_body, 'plain', 'utf-8')
        msg['title']='重置密码'
        msg['From'] = '1904258580@qq.com <1904258580@qq.com>'
        msg['Subject'] = Header(u'text', 'utf8').encode()
        msg['To'] = email
        server.sendmail('1904258580@qq.com', [email], msg.as_string())
        server.quit()
    if send_type==3:
        send_title = '修改邮箱'
        send_body = send_title + '邮箱验证码:\n' + a.code
        msg = MIMEText(send_body, 'plain', 'utf-8')
        msg['title'] = '修改邮箱'
        msg['From'] = '1904258580@qq.com <1904258580@qq.com>'
        msg['Subject'] = Header(u'text', 'utf8').encode()
        msg['To'] = email
        server.sendmail('1904258580@qq.com', [email], msg.as_string())
        server.quit()







