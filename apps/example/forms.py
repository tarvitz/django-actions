# coding: utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from apps.actions.forms import ActionForm
from apps.example.models import Category

class ChangePostActionForm(ActionForm):
    author = forms.ModelChoiceField(queryset=User.objects, required=False)
    ip_addr = forms.IPAddressField()
    category = forms.ModelChoiceField(queryset=Category.objects, required=False)
