from django.urls import include, re_path

urlpatterns = [
    # system
    re_path(r'^user/', include('user.urls')),
]