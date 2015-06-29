# -- coding: utf-8 --

__author__ = 'amryfitra'

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.forms.models import modelform_factory
from django.contrib import messages

from .forms import CattleForm, NeckbandPatternForm

from .models import Place, Stall, Cattle, NeckbandPattern, CattleNeckband
import datetime
import time
import random

def ca_index(request):
    place_count = Place.objects.count()
    stall_count = Stall.objects.count()
    cattle_count = Cattle.objects.count()
    """
    lineChart page
    """
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    nb_element = 150
    xdata = range(nb_element)
    xdata = list(map(lambda x: start_time + x * 1000000000, xdata))
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = list(map(lambda x: x * 2, ydata))

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie1 = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "date_format": tooltip_date,
        'color': '#a4c639'
    }
    extra_serie2 = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "date_format": tooltip_date,
        'color': '#FF8aF8'
    }
    chartdata = {'x': xdata,
                 'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie1,
                 'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie2}

    charttype = "lineChart"
    chartcontainer = 'linechart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d %b %Y %H',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }

    return render_to_response("core_app/index.html", data,
                              context_instance=RequestContext(request))

def place_index(request):

    places = Place.objects.all()
    cur_path = request.get_full_path()
    context = {
        "cur_path": cur_path,
        "places": places
    }

    return render_to_response("core_app/place_index.html", context,
                              context_instance=RequestContext(request))

def place_add(request):
    url_next = request.GET.get("next")
    PlaceForm = modelform_factory(Place, fields="__all__")

    if request.method == "POST":
        place_form = PlaceForm(request.POST)
        if place_form.is_valid():
            place_form.save()
        else:
            for k, v in place_form.errors.items():
                messages.error(request, "{}: {}".format(k,v))
        return redirect(url_next)
    else:
        place_form = PlaceForm()

    context = {
        "url_next": url_next,
        "place_form": place_form
    }

    return render_to_response("core_app/place_add.html", context,
                              context_instance=RequestContext(request))

def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    stalls = place.stall_set.all()
    cur_path = request.get_full_path()
    context = {
        "place": place,
        "stalls": stalls,
        "cur_path": cur_path
    }

    return render_to_response("core_app/place_detail.html", context,
                              context_instance=RequestContext(request))

def stall_index(request):

    stalls = Stall.objects.all()
    cur_path = request.get_full_path()
    context = {
        "cur_path": cur_path,
        "stalls": stalls
    }

    return render_to_response("core_app/stall_index.html", context,
                              context_instance=RequestContext(request))

def stall_add(request):
    url_next = request.GET.get("next")
    place = None

    if "place_id" in request.GET.keys():
        place = get_object_or_404(Place, pk=int(request.GET["place_id"]))
        StallForm = modelform_factory(Stall, exclude=["place"])
    else:
        StallForm = modelform_factory(Stall, fields="__all__")

    if request.method == "POST":
        stall_form = StallForm(request.POST)
        if stall_form.is_valid():
            stall = stall_form.save(commit=False)
            if place:
                stall.place = place
            stall.save()
            messages.info(request, '{} created!'.format(stall.name))
        else:
            for k, v in stall_form.errors.items():
                messages.error(request, "{}: {}".format(k,v))
        return redirect(url_next)
    else:
        stall_form = StallForm()

    context = {
        "place": place,
        "url_next": url_next,
        "stall_form": stall_form
    }

    return render_to_response("core_app/stall_add.html", context,
                              context_instance=RequestContext(request))

def stall_detail(request, stall_id):

    stall = get_object_or_404(Stall, pk=stall_id)
    lst_cattle = stall.cattle_set.all()
    cur_path = request.get_full_path()
    context = {
        "stall": stall,
        "lst_cattle": lst_cattle,
        "cur_path": cur_path
    }

    return render_to_response("core_app/stall_detail.html", context,
                              context_instance=RequestContext(request))


def cattle_index(request):
    lst_cattle = Cattle.objects.all()
    cur_path = request.get_full_path()
    context = {
        "cur_path": cur_path,
        "lst_cattle": lst_cattle
    }

    return render_to_response("core_app/cattle_index.html", context,
                              context_instance=RequestContext(request))

def cattle_add(request):
    url_next = request.GET.get("next")
    stall = None

    if "stall_id" in request.GET.keys():
        stall = get_object_or_404(Stall, pk=int(request.GET["stall_id"]))
        CattleForm = modelform_factory(Cattle, exclude=["stall"])
    else:
        CattleForm = modelform_factory(Cattle, fields="__all__")

    if request.method == "POST":
        cattle_form = CattleForm(request.POST)
        if cattle_form.is_valid():
            cattle = cattle_form.save(commit=False)
            if stall:
                cattle.stall = stall
            cattle.save()
            messages.info(request, '{} created!'.format(cattle.id_number))
        else:
            for k, v in cattle_form.errors.items():
                messages.error(request, "{}: {}".format(k,v))
        return redirect(url_next)
    else:
        cattle_form = CattleForm()

    context = {
        "stall": stall,
        "url_next": url_next,
        "cattle_form": cattle_form
    }

    return render_to_response("core_app/cattle_add.html", context,
                              context_instance=RequestContext(request))

def cattle_detail(request, cattle_id):
    cattle = get_object_or_404(Cattle, pk=cattle_id)
    catle_neckband_patterns = cattle.cattleneckband_set.all()
    cur_path = request.get_full_path()

    CattleNeckbandForm = modelform_factory(CattleNeckband, exclude=["cattle"])

    if request.method == "POST":
        neckband_form = CattleNeckbandForm(request.POST)
        if neckband_form.is_valid():
            neckband = neckband_form.save(commit=False)
            neckband.cattle = cattle
            neckband.save()
            return redirect("ca_cattle_detail", cattle_id=cattle_id)

    neckband_form = CattleNeckbandForm()
    context = {
        "cur_path": cur_path,
        "cattle": cattle,
        "cattle_neckband_patterns": catle_neckband_patterns,
        "neckband_form": neckband_form,
    }

    return render_to_response("core_app/cattle_detail.html", context,
                              context_instance=RequestContext(request))

def neckband_index(request):
    lst_neckband = NeckbandPattern.objects.all()
    cur_path = request.get_full_path()
    context = {
        "cur_path": cur_path,
        "lst_neckband": lst_neckband
    }

    return render_to_response("core_app/neckband_index.html", context,
                              context_instance=RequestContext(request))

def neckband_add(request):
    url_next = request.GET.get("next")
    NeckbandForm = modelform_factory(NeckbandPattern, fields="__all__")

    if request.method == "POST":
        neckband_form = NeckbandForm(request.POST)
        if neckband_form.is_valid():
            neckband_form.save()
        else:
            for k, v in neckband_form.errors.items():
                messages.error(request, "{}: {}".format(k,v))
        return redirect(url_next)
    else:
        neckband_form = NeckbandForm()

    context = {
        "url_next": url_next,
        "neckband_form": neckband_form
    }

    return render_to_response("core_app/neckband_add.html", context,
                              context_instance=RequestContext(request))

def neckband_detail(request, neckband_id):
    neckband = get_object_or_404(NeckbandPattern, pk=neckband_id)
    lst_cattle_neckband = neckband.cattleneckband_set.all()
    cur_path = request.get_full_path()
    context = {
        "neckband": neckband,
        "lst_cattle_neckband": lst_cattle_neckband,
        "cur_path": cur_path
    }

    return render_to_response("core_app/neckband_detail.html", context,
                              context_instance=RequestContext(request))