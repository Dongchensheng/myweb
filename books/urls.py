from django.conf.urls import url
from books.views import table, upload, upload_save
urlpatterns = [
    url(r'^$', table, name='table'),
    url(r'^table/$', table, name='table'),
    url(r'^upfile/$', upload, name='upload'),
    url(r'^upload_s/$', upload_save, name='upload'),
]