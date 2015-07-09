# -- coding: utf-8 --

__author__ = 'amryfitra'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^device/$', views.device_index, name="da_device_index"),
    url(r'^device/(?P<device_id>\w+)/$', views.device_detail, name="da_device_detail"),
    url(r'^condition/add$', views.device_condition_add, name="da_condition_add"),
    url(r'^error/add$', views.device_error_add, name="da_error_add"),
    url(r'^log/add$', views.device_log_add, name="da_log_add"),
]