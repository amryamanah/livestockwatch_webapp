# -- coding: utf-8 --

__author__ = 'amryfitra'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cattle/$', views.cattle_index, name="ca_cattle_index"),
    url(r'^cattle/add/$', views.cattle_add, name="ca_cattle_add"),
    url(r'^cattle/(?P<cattle_id>\w+)/$', views.cattle_detail, name="ca_cattle_detail"),
    url(r'^neckband/$', views.neckband_index, name="ca_neckband_index"),
    url(r'^neckband/add/$', views.neckband_add, name="ca_neckband_add"),
    url(r'^neckband/(?P<neckband_id>\w+)/$', views.neckband_detail, name="ca_neckband_detail"),
    url(r'^blooddata1/add/$', views.blood_data1_add, name="ca_blooddata1_add"),
    url(r'^blooddata2/add/$', views.blood_data2_add, name="ca_blooddata2_add"),
    url(r'^bodydata1/add/$', views.body_data1_add, name="ca_bodydata1_add"),
    url(r'^bodydata2/add/$', views.body_data2_add, name="ca_bodydata2_add"),
    url(r'^cattleneckband/add/$', views.cattle_neckband_add, name="ca_cattleneckband_add"),
    url(r'^bodytemp/add/$', views.body_temp_add, name="ca_bodytemp_add"),
]