# -*- coding: utf-8 -*-
# Author： fangfu

from django import forms


class UserLogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) # 为form类字段指定类型