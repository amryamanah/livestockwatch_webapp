# -- coding: utf-8 --

__author__ = 'amryfitra'

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.forms.models import modelform_factory
from django.contrib import messages

from .models import Cattle, NeckbandPattern, CattleNeckband, BloodData1, \
    BloodData2, BodyData1, BodyData2, BodyTemp
from farm_app.models import Stall

def cattle_index(request):
    lst_cattle = Cattle.objects.all()
    cur_path = request.get_full_path()
    context = {
        "cur_path": cur_path,
        "lst_cattle": lst_cattle
    }

    return render_to_response("cattle_app/cattle_index.html", context,
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

    return render_to_response("cattle_app/cattle_add.html", context,
                              context_instance=RequestContext(request))

def cattle_detail(request, cattle_id):
    cattle = get_object_or_404(Cattle, pk=cattle_id)
    cattle_neckband_patterns = cattle.cattleneckband_set.all()
    lst_blood_data1 = cattle.blooddata1_set.all()
    lst_blood_data2 = cattle.blooddata2_set.all()
    lst_body_data1 = cattle.bodydata1_set.all()
    lst_body_data2 = cattle.bodydata2_set.all()
    lst_body_temp = cattle.bodytemp_set.all()
    lst_feed_data = cattle.feeddata_set.all()
    lst_remarks_data = cattle.remarksdata_set.all()
    lst_bodytemp = cattle.bodytemp_set.all()
    lst_capture_session = cattle.capturesession_set.all()
    cur_path = request.get_full_path()

    context = {
        "cur_path": cur_path,
        "cattle": cattle,
        "lst_bodytemp": lst_bodytemp,
        "cattle_neckband_patterns": cattle_neckband_patterns,
        "lst_blood_data1": lst_blood_data1,
        "lst_blood_data2": lst_blood_data2,
        "lst_body_data1": lst_body_data1,
        "lst_body_data2": lst_body_data2,
        "lst_body_temp": lst_body_temp,
        "lst_feed_data": lst_feed_data,
        "lst_remarks_data": lst_remarks_data,
        "lst_capture_session": lst_capture_session
    }

    return render_to_response("cattle_app/cattle_detail.html", context,
                              context_instance=RequestContext(request))

def cattle_neckband_add(request):
    url_next = request.GET.get("next")
    cattle = get_object_or_404(Cattle, pk=int(request.GET["cattle_id"]))
    CattleNeckbandForm = modelform_factory(CattleNeckband, exclude=["cattle"])

    if request.method == "POST":
        form = CattleNeckbandForm(request.POST)
        if form.is_valid():
            cattle_neckband = form.save(commit=False)
            cattle_neckband.cattle = cattle
            cattle_neckband.save()
        else:
            for k, v in form.errors.items():
                messages.error(request, "{}: {}".format(k,v))
        return redirect(url_next)
    else:
        form = CattleNeckbandForm()

    context = {
        "url_next": url_next,
        "cattle": cattle,
        "form": form
    }

    return render_to_response("cattle_app/cattle_neckband_add.html", context,
                              context_instance=RequestContext(request))


def neckband_index(request):
    lst_neckband = NeckbandPattern.objects.all()
    cur_path = request.get_full_path()
    context = {
        "cur_path": cur_path,
        "lst_neckband": lst_neckband
    }

    return render_to_response("cattle_app/neckband_index.html", context,
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

    return render_to_response("cattle_app/neckband_add.html", context,
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

    return render_to_response("cattle_app/neckband_detail.html", context,
                              context_instance=RequestContext(request))

def blood_data1_add(request):
    url_next = request.GET.get("next")
    cattle = get_object_or_404(Cattle, pk=int(request.GET["cattle_id"]))
    BloodData1Form = modelform_factory(BloodData1, exclude=["cattle"])

    if request.method == "POST":
        form = BloodData1Form(request.POST)
        if form.is_valid():
            blood_data1 = form.save(commit=False)
            blood_data1.cattle = cattle
            blood_data1.save()
        else:
            for k, v in form.errors.items():
                messages.error(request, "{}: {}".format(k,v))
        return redirect(url_next)
    else:
        form = BloodData1Form()

    context = {
        "url_next": url_next,
        "cattle": cattle,
        "form": form
    }

    return render_to_response("cattle_app/blood_data1_add.html", context,
                              context_instance=RequestContext(request))

def blood_data2_add(request):
    url_next = request.GET.get("next")
    cattle = get_object_or_404(Cattle, pk=int(request.GET["cattle_id"]))
    BloodData2Form = modelform_factory(BloodData2, exclude=["cattle"])

    if request.method == "POST":
        form = BloodData2Form(request.POST)
        if form.is_valid():
            blood_data2 = form.save(commit=False)
            blood_data2.cattle = cattle
            blood_data2.save()
        else:
            for k, v in form.errors.items():
                messages.error(request, "{}: {}".format(k,v))
        return redirect(url_next)
    else:
        form = BloodData2Form()

    context = {
        "url_next": url_next,
        "cattle": cattle,
        "form": form
    }

    return render_to_response("cattle_app/blood_data2_add.html", context,
                              context_instance=RequestContext(request))

def body_data1_add(request):
    url_next = request.GET.get("next")
    cattle = get_object_or_404(Cattle, pk=int(request.GET["cattle_id"]))
    BodyData1Form = modelform_factory(BodyData1, exclude=["cattle"])

    if request.method == "POST":
        form = BodyData1Form(request.POST)
        if form.is_valid():
            body_data1 = form.save(commit=False)
            body_data1.cattle = cattle
            body_data1.save()
        else:
            for k, v in form.errors.items():
                messages.error(request, "{}: {}".format(k,v))
        return redirect(url_next)
    else:
        form = BodyData1Form()

    context = {
        "url_next": url_next,
        "cattle": cattle,
        "form": form
    }

    return render_to_response("cattle_app/body_data1_add.html", context,
                              context_instance=RequestContext(request))

def body_data2_add(request):
    url_next = request.GET.get("next")
    cattle = get_object_or_404(Cattle, pk=int(request.GET["cattle_id"]))
    BodyData2Form = modelform_factory(BodyData2, exclude=["cattle"])

    if request.method == "POST":
        form = BodyData2Form(request.POST)
        if form.is_valid():
            body_data2 = form.save(commit=False)
            body_data2.cattle = cattle
            body_data2.save()
        else:
            for k, v in form.errors.items():
                messages.error(request, "{}: {}".format(k, v))
        return redirect(url_next)
    else:
        form = BodyData2Form()

    context = {
        "url_next": url_next,
        "cattle": cattle,
        "form": form
    }

    return render_to_response("cattle_app/body_data2_add.html", context,
                              context_instance=RequestContext(request))

def body_temp_add(request):
    url_next = request.GET.get("next")
    cattle = get_object_or_404(Cattle, pk=int(request.GET["cattle_id"]))
    BodyTempForm = modelform_factory(BodyTemp, exclude=["cattle"])

    if request.method == "POST":
        form = BodyTempForm(request.POST)
        if form.is_valid():
            body_temp = form.save(commit=False)
            body_temp.cattle = cattle
            body_temp.save()
        else:
            for k, v in form.errors.items():
                messages.error(request, "{}: {}".format(k, v))
        return redirect(url_next)
    else:
        form = BodyTempForm()

    context = {
        "url_next": url_next,
        "cattle": cattle,
        "form": form
    }

    return render_to_response("cattle_app/body_temp_add.html", context,
                              context_instance=RequestContext(request))