# -- coding: utf-8 --

__author__ = 'amryfitra'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^place/$', views.place_index, name="fa_place_index"),
    url(r'^place/add/$', views.place_add, name="fa_place_add"),
    url(r'^place/(?P<place_id>\w+)/$', views.place_detail, name="fa_place_detail"),
    url(r'^stall/$', views.stall_index, name="fa_stall_index"),
    url(r'^stall/add/$', views.stall_add, name="fa_stall_add"),
    url(r'^stall/(?P<stall_id>\w+)/$', views.stall_detail, name="fa_stall_detail")
]