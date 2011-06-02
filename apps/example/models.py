# coding: utf8
from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext as _tr
from django.contrib.auth.models import User
from apps.actions.actions import common_delete_action

class Category(models.Model):
    title = models.CharField(_('Title'), unique=True, max_length=64)
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
    __unicode__ = lambda s: s.title

class Post(models.Model):
    from apps.example.actions import change_post_action
    title = models.CharField(_('Title'), max_length=128)
    category = models.ForeignKey(Category, help_text=('Post category'))
    content = models.TextField(_('Content'), max_length=10240)
    author = models.ForeignKey(User)
    ip_addr = models.IPAddressField(_('IP address'))
    
    common_delete_action.has_perms = ['example.delete_post', ]
    actions = [common_delete_action, change_post_action]
    __unicode__ = lambda s: s.title
