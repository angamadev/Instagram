from django import forms
from django.forms import ModelForm
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _lazy
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from posts.models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [   
            "image",
            "description",
            ]
