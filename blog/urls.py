from django.conf.urls import url
from blog.views import index, login, logout, login_action
urlpatterns = [
    url(r'^$', login, name='login'),
    url(r'^index/$', index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^login_action/$', login_action, name='login_action'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^accounts/login/$', login, name='login'),
]