# -- coding: utf-8 --

__author__ = 'amryfitra'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^capture_session/$',
        views.capture_session_index, name="ia_capture_session_index"),
    url(r'^capture_session/add/$', views.capture_session_add, name="ia_capture_session_add"),
    url(r'^capture_session/(?P<capture_session_id>\w+)/details/$',
        views.capture_session_details, name="ia_capture_session_details"),
    url(r'^analysis_session/$',
        views.analysis_session_index, name="ia_analysis_session_index"),
    url(r'^analysis_session/(?P<analysis_session_id>\d+)/$',
        views.analysis_session_detail, name="ia_analysis_session_detail"),
    url(r'^analysis_session/(?P<analysis_session_id>\d+)/run_pupil_analysis/$',
        views.pupil_analysis_runner, name="ia_pupil_analysis_runner"),
    url(r'^analysis_session/(?P<analysis_session_id>\d+)/analysis_parameter/(?P<analysis_param_id>\d+)/$',
        views.analysis_result_detail, name="ia_analysis_result_detail")
]

