from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.forms.models import modelform_factory
from django.contrib import messages

from device_app.models import Device

from .models import Place, Stall
from .forms import  NewStallForm, NewStallFormWoPlace

def place_index(request):

    places = Place.objects.all()
    cur_path = request.get_full_path()
    context = {
        "cur_path": cur_path,
        "places": places
    }

    return render_to_response("farm_app/place_index.html", context,
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

    return render_to_response("farm_app/place_add.html", context,
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

    return render_to_response("farm_app/place_detail.html", context,
                              context_instance=RequestContext(request))

def stall_index(request):

    stalls = Stall.objects.all()
    cur_path = request.get_full_path()
    context = {
        "cur_path": cur_path,
        "stalls": stalls
    }

    return render_to_response("farm_app/stall_index.html", context,
                              context_instance=RequestContext(request))

def stall_add(request):
    url_next = request.GET.get("next")
    place = None

    if "place_id" in request.GET.keys():
        place = get_object_or_404(Place, pk=int(request.GET["place_id"]))
        StallForm = NewStallFormWoPlace
    else:
        StallForm = NewStallForm

    if request.method == "POST":
        stall_form = StallForm(request.POST)
        if stall_form.is_valid():
            stall = stall_form.save(commit=False)
            if place:
                stall.place = place
            stall.save()
            device, created = Device.objects.get_or_create(
                name=stall_form.cleaned_data["device_name"],
                stall=stall
            )

            messages.info(request, '{} created!'.format(stall.name))
            messages.info(request, '{} device created!'.format(device.name))
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

    return render_to_response("farm_app/stall_add.html", context,
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

    return render_to_response("farm_app/stall_detail.html", context,
                              context_instance=RequestContext(request))