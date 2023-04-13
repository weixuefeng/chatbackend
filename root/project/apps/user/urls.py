from django.urls import include, re_path, path
from user import apis

urlpatterns = [
    re_path(r'^$', apis.api_ping),
    re_path(r'^login/$', apis.api_login),
    re_path(r'^completions/$', apis.completions),
    re_path(r'chat/$', apis.chat),
    re_path(r'images/$', apis.images),
]
