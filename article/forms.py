# -*- encoding: utf-8 -*-
from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, required=True, error_messages={"required": "请填写您的名字"})
    email = forms.EmailField(required=True, error_messages={"required": "请填写您的邮箱"})
    to = forms.EmailField(required=True, error_messages={"required": "请填写您的收件人邮箱"})
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        # 指定model
        model = Comment
        # 默认加载所有字段，这里手动指定所需填写的字段
        fields = ('name', 'email', 'body')
