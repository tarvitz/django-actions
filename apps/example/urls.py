from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('apps.example.views',
    url(r'^$', 'index', name='url_index'),
)
