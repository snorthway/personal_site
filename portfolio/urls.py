from django.conf.urls import patterns, url
from portfolio import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^engineering/$', views.engineering, name='engineering'),
    url(r'^photography/$', views.photography, name='photography'),
    # This is fucking ugly
    url(r'^photography/(?P<subcategory>\w+)/$', views.album, {'subcategory':'portraits'},name='album'),
    url(r'^photography/(?P<subcategory>\w+)/$', views.album, {'subcategory':'nature'},name='album'),
    url(r'^photography/(?P<subcategory>\w+)/$', views.album, {'subcategory':'etcetera'},name='album'),
    url(r'^sketchbook/$', views.sketchbook, name='sketchbook'),
)