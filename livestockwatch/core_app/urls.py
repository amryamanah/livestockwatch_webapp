# -- coding: utf-8 --

__author__ = 'amryfitra'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ca_index, name="ca_index"),
    url(r'^place/$', views.place_index, name="ca_place_index"),
    url(r'^place/add/$', views.place_add, name="ca_place_add"),
    url(r'^place/(?P<place_id>\w+)/$', views.place_detail, name="ca_place_detail"),
    url(r'^stall/$', views.stall_index, name="ca_stall_index"),
    url(r'^stall/add/$', views.stall_add, name="ca_stall_add"),
    url(r'^stall/(?P<stall_id>\w+)/$', views.stall_detail, name="ca_stall_detail"),
    url(r'^cattle/$', views.cattle_index, name="ca_cattle_index"),
    url(r'^cattle/add/$', views.cattle_add, name="ca_cattle_add"),
    url(r'^cattle/(?P<cattle_id>\w+)/$', views.cattle_detail, name="ca_cattle_detail"),
    url(r'^neckband/$', views.neckband_index, name="ca_neckband_index"),
    url(r'^neckband/add/$', views.neckband_add, name="ca_neckband_add"),
    url(r'^neckband/(?P<neckband_id>\w+)/$', views.neckband_detail, name="ca_neckband_detail")
]