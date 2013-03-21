from django.conf.urls import patterns, url
from portfolio import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^engineering/$', views.engineering, name='engineering'),
    url(r'^photography/$', views.photography, name='photography'),
    url(r'^photography/portraits/$', views.album, name='portraits'),
    url(r'^sketchbook/$', views.sketchbook, name='sketchbook'),
)