# coding: utf8
#
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from apps.actions.forms import action_formset
from apps.actions.helpers import get_content_type_or_404

def act(request, app_n_model):
    """ execute chosen action """
    ct = get_content_type_or_404(app_n_model)
    app, model = app_n_model.split('.')
    if request.method == 'POST':
        qset = ct.model_class().objects.filter(pk__in=(request.POST.getlist('items')))
        formclass = action_formset(request, qset, ct.model_class())
        form = formclass(request.POST)
        if form.is_valid():
            #items = ct.model_class().objects.filter(pk__in=(request.POST.get('items', None)))
            qset = form.act(form.cleaned_data['action'], form.cleaned_data['items'])
            if 'response' in qset: return qset['response']
            return HttpResponseRedirect('/success')
        else:       
            return HttpResponseRedirect('/failed')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
