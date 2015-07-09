from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^device_condition/$', views.device_condition_list, name="api_device_condition"),
    url(r'^device_error/$', views.device_error_list, name="api_device_error")
]

urlpatterns = format_suffix_patterns(urlpatterns)