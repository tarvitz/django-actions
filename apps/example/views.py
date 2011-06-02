# coding: utf8

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.actions.forms import action_formset
from apps.example.models import Post
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def index(request):
    template = 'index.html'
    posts = Post.objects.all()
    formclass = action_formset(request, posts, Post,
        permissions=['actions.delete_post', 'actions.change_post'])
    form = formclass(request.POST or None) 
    if request.method == 'POST':
        if form.is_valid():
            qset = form.act(form.cleaned_data['action'],
                form.cleaned_data['items'])
            if 'response' in qset: return qset['response']
            return HttpResponseRedirect(reverse('url_index'))
        else:
            return render_to_response(template, {'posts': posts, 'form': form},
        context_instance=RequestContext(request))
    return render_to_response(template, {'posts': posts, 'form': form},
        context_instance=RequestContext(request))

def idx(request):
    template = 'idx.html'
    posts = Post.objects.all()
    return render_to_response(template, {'posts': posts},
        context_instance=RequestContext(request))

