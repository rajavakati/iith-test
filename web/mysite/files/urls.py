from django.conf.urls import patterns, url

from files import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^/index1/$', views.index1, name='index1'),
    url(r'^frequency/$', views.frequency, name='frequency'),
    url(r'^sizes/$', views.sizes, name='sizes'),
)
