# _*_ coding:utf-8 _*_
__auther__ = 'xiaotang'
__date__ = '2017/12/2 17:46'
from django import forms


class MessagesForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    want = forms.CharField(required=True)
