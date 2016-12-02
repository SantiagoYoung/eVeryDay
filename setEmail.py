# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives, mail_admins, send_mail, send_mass_mail

def setEmail(request):

    if request.method == 'POST':

        # 方式一：
        #     from django.core.mail import send_mail
        #     send_mail('subject', 'this is the message of email', 'sender@gamil.com',
        #                 ['123@qq.com', '456@qq.com'], fail_silently=False)
        #
        # 方式二：
        #     message1 = ('subject', 'text', 'sender@gmail.com',
        #                 ['123@qq.com', '456@qq.com'] )
        #     message2 = ('subject', 'text', 'sender@gmail.com',
        #                 ['567@qq.com', '789@qq.com'] )
        #     send_mass_mail((message1, message2), fail_silently=False)
        #
        # 方式三： 防止邮件头注入
        #     try:
        #         send_mail(subject, message, from_email, recipient_list, fail_silently, auth_user, auth_password, connection)
        #     except BadHeaderError:
        #         return HttpResponse('Invalid header fount.')
        # 方式四: EmailMessage()
        #     #首先实例化一个EmaiMessage()对象
        #     em = EmailMessage('subject', 'body', 'from@qq.com', ['123@qq.com'],['456@qq.com'], header={'Reply-to': 'another@qq.com'})
        #     #调用相应的方法
        #
        # 方式五：发送多用途邮件

        subject, from_email, to = 'hello', 'from@qq.com', '23@qq.com'
        text_content = 'This is an important message'
        html_content = u"<b>激活链接:</b><a href='http://www.baidu.com'>http:www.baidu.com</a>"
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

#       发送邮件成功给管理员发送一个反馈
        mail_admins(u'用户注册反馈', u'当前xx用户注册成功', fail_silently = True)
        return HttpResponse('success')
    return render(request,'')








