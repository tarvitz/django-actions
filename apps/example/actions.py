#coding: utf8
from django.utils.translation import ugettext_lazy as _, ugettext as _tr
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from apps.example.forms import ChangePostActionForm

def change_post_action(request, qset, model, **kwargs):
    template = 'actions/change_post_form.html'
    if request.method == 'POST':
        form = ChangePostActionForm(request.POST, model=model, qset=qset)
        if form.is_valid():
            for q in qset:
                q.author = form.cleaned_data.get('author', None) or q.author
                q.ip_addr = form.cleaned_data['ip_addr']
                q.category = form.cleaned_data.get('category', None) or q.category
                q.save()
            return {'qset': qset}
        else: 
            return {'response': render_to_response(template,
                {'form': form},
                context_instance=RequestContext(request))}
    return {'qset': qset }
change_post_action.short_description = _('change post')
change_post_action.has_perms = ['example.change_post',]
