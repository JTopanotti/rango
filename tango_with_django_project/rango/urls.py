from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^goto/', views.track_url, name='goto'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
        url(r'^restricted/$', views.restricted, name='restricted'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
        url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/(?P<template_name>[A-Za-z_./]+)/$',
                auth_views.password_reset_confirm, name='password_reset_confirm'),
        url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
        url(r'^profile/$', views.profile, name="profile"),
        url(r'^logout/$', views.user_logout, name='logout'),
]        
