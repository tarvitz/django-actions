# coding: utf8
from django.http import Http404
from django.contrib.contenttypes.models import ContentType
def get_content_type(obj):
    app_label, model = obj.split('.')
    return ContentType.objects.get(app_label=app_label, model=model)

def get_content_type_or_404(obj):
    """ simple return content_type of given model's application"""
    try:
        return get_content_type(obj)        
    except:
        raise Http404("There is no such content type with given '%s'" % obj)

def get_content_type_or_None(obj):
    try:
        return get_content_type(obj)
    except:
        return None

def parse_perms(perms, app, model):
    _perms = []
    for p in perms:
        _perms.append(p.format(app=app, model=model))
    return _perms
