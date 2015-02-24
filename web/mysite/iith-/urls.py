from django.conf.urls import patterns, include, url
from iith import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^frequencies/',iith.line_chart, name='line_chart'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^sizes/', iith.pie_chart,name='pie_chart'),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
