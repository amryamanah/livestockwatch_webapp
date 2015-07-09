from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.forms.models import modelform_factory
from django.contrib import messages

from .models import Device, DeviceCondition, DeviceError, DeviceLog


def device_index(request):

    lst_device = Device.objects.all()
    cur_path = request.get_full_path()
    context = {
        "cur_path": cur_path,
        "lst_device": lst_device
    }

    return render_to_response("device_app/device_index.html", context,
                              context_instance=RequestContext(request))


def device_detail(request, device_id):
    cur_path = request.get_full_path()
    device = get_object_or_404(Device, pk=device_id)
    lst_device_error = device.deviceerror_set.order_by("-time_taken").all()
    lst_device_condition = device.devicecondition_set.order_by("-time_taken").all()
    lst_device_log = device.devicelog_set.order_by("-time_taken").all()

    context = {
        "cur_path": cur_path,
        "device": device,
        "lst_device_error": lst_device_error,
        "lst_device_condition": lst_device_condition,
        "lst_device_log": lst_device_log
    }

    return render_to_response("device_app/device_detail.html", context,
                              context_instance=RequestContext(request))

def device_condition_add(request):
    url_next = request.GET.get("next")
    device = get_object_or_404(Device, pk=int(request.GET["device_id"]))
    DeviceConditionForm = modelform_factory(DeviceCondition, exclude=["device"])

    if request.method == "POST":
        form = DeviceConditionForm(request.POST)
        if form.is_valid():
            condition = form.save(commit=False)
            condition.device = device
            condition.save()
        else:
            for k, v in form.errors.items():
                messages.error(request, "{}: {}".format(k, v))
        return redirect(url_next)
    else:
        form = DeviceConditionForm()

    context = {
        "url_next": url_next,
        "device": device,
        "form": form
    }

    return render_to_response("device_app/device_condition_add.html", context,
                              context_instance=RequestContext(request))

def device_error_add(request):
    url_next = request.GET.get("next")
    device = get_object_or_404(Device, pk=int(request.GET["device_id"]))
    DeviceErrorForm = modelform_factory(DeviceError, exclude=["device"])

    if request.method == "POST":
        form = DeviceErrorForm(request.POST)
        if form.is_valid():
            condition = form.save(commit=False)
            condition.device = device
            condition.save()
        else:
            for k, v in form.errors.items():
                messages.error(request, "{}: {}".format(k, v))
        return redirect(url_next)
    else:
        form = DeviceErrorForm()

    context = {
        "url_next": url_next,
        "device": device,
        "form": form
    }

    return render_to_response("device_app/device_error_add.html", context,
                              context_instance=RequestContext(request))

def device_log_add(request):
    url_next = request.GET.get("next")
    device = get_object_or_404(Device, pk=int(request.GET["device_id"]))
    DeviceLogForm = modelform_factory(DeviceLog, exclude=["device"])

    if request.method == "POST":
        form = DeviceLogForm(request.POST)
        if form.is_valid():
            condition = form.save(commit=False)
            condition.device = device
            condition.save()
        else:
            for k, v in form.errors.items():
                messages.error(request, "{}: {}".format(k, v))
        return redirect(url_next)
    else:
        form = DeviceLogForm()

    context = {
        "url_next": url_next,
        "device": device,
        "form": form
    }

    return render_to_response("device_app/device_log_add.html", context,
                              context_instance=RequestContext(request))

