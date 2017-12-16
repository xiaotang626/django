# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.core.mail import send_mail
from untitled1.settings import EMAIL_FROM
from blog.forms import MessagesForm

from blog.models import Banner, Narration, Work, Comic, Make


class IndexView(View):
    def get(self, request):
        # 轮播图
        banners = Banner.objects.all()

        # 简介
        narration_fs = Narration.objects.all()[:3]
        narration_ds = Narration.objects.all()[3:]

        # 工作
        works = Work.objects.all()

        # 制作
        makes = Make.objects.all()

        return render(request, 'index.html', {
            'banners': banners,
            'narration_fs': narration_fs,
            'narration_ds': narration_ds,
            'works': works,
            'makes': makes,

        })

    def post(self, request):
        messages_form = MessagesForm(request.POST)
        if messages_form.is_valid():
            # 发给收件人
            email_title = request.POST.get('name', '')
            email_body = '谢谢你，我已经收到了你的邮件，我会认真看你的来信的，希望你有一个好心情😊'
            email = request.POST.get('email', '')  # 对方的邮箱
            send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
            # 发给自己对方说的话
            email2 = '1119032205@qq.com'
            email_body2 = request.POST.get('want', '') + str(request.POST.get('email', ''))
            send_status2 = send_mail(email_title, email_body2, EMAIL_FROM, [email2])

            if send_status and send_status2:
                pass

                # 轮播图
                comics = Comic.objects.all()

                return render(request, 'send_success.html', {
                    'comics': comics,
                })
        else:
            messages_form = MessagesForm(request.POST)

            return render(request, 'send_filed.html', {
                'messages_form': messages_form,
            })
