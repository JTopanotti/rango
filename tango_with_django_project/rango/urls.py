from django.conf.urls import url
from . import views
from django.conf.urls import include

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url('^', include('django.contrib.auth.urls')),
        url(r'^about/$', views.about, name='about'),
        url(r'^goto/', views.track_url, name='goto'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
        url(r'^restricted/$', views.restricted, name='restricted'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
]        
