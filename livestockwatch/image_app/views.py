from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.conf import settings
from django.forms.models import modelform_factory

from datetime import datetime
import time
import cv2
import os
import random

from cattle_app.models import Cattle

from .pupil_analysis import detect_pupil, NoPupilDetected, \
    ImpartialPupilDetected, EllipseAnalysis, ellipse_calculate_ca, ellipse_normalized_area, save_pupil_analysis_result
from .models import RawImage, CaptureSession, ImageAnalysisSession, \
    ImageAnalysisParameter, ImageAnalysisResult, AnalysisCaptureSessionResult
from .forms import RawImageUploadForm, ImageAnalysisSessionForm, \
    ImageAnalysisParameterForm, RawImageUploadFormWithCattle

def capture_session_index(request):
    cur_path = request.get_full_path()

    capture_sessions = CaptureSession.objects.order_by("time_taken").all()

    context = {
        "cur_path": cur_path,
        "capture_sessions": capture_sessions
    }

    return render_to_response("image_app/capture_session_index.html", context,
                              context_instance=RequestContext(request))


def capture_session_add(request):
    url_next = request.GET.get("next")
    cattle = None

    if "cattle_id" in request.GET.keys():
        cattle = get_object_or_404(Cattle, pk=int(request.GET["cattle_id"]))
        CaptureSessionForm = RawImageUploadForm
    else:
        CaptureSessionForm = RawImageUploadFormWithCattle

    if request.method == "POST":
        capture_session_form = CaptureSessionForm(request.POST, request.FILES)

        if capture_session_form.is_valid():
            period = capture_session_form.cleaned_data["period_of_the_day"]
            names = sorted([im.name for im in capture_session_form.cleaned_data["image_files"]])
            filename_part = names[0].split("_")
            capture_session_name = "_".join([
                filename_part[1],
                filename_part[2],
                filename_part[3],
                filename_part[4],
                filename_part[5],
                filename_part[6],
                filename_part[7]
            ])
            if capture_session_name.endswith(".bmp"):
                capture_session_name = capture_session_name.split(".bmp")[0]

            if not cattle:
                cattle = capture_session_form.cleaned_data["cattle"]

            capture_session, created = CaptureSession.objects.get_or_create(
                cattle=cattle,
                name=capture_session_name,
                period=period,
                time_taken=datetime.strptime(capture_session_name, '%Y_%m_%d_%H_%M_%S_%f')
            )

            for image in capture_session_form.cleaned_data["image_files"]:
                try:
                    RawImage.objects.get(name=image.name, capture_session=capture_session)
                except RawImage.DoesNotExist:
                    RawImage.objects.create(
                        capture_session=capture_session,
                        image_file=image
                    )

            return redirect(url_next)
    else:
        capture_session_form = CaptureSessionForm()

    context = {
        "url_next": url_next,
        "cattle": cattle,
        "capture_session_form": capture_session_form
    }

    return render_to_response("image_app/capture_session_add.html", context,
                              context_instance=RequestContext(request))


def capture_session_details(request, capture_session_id):
    capture_session = get_object_or_404(CaptureSession, pk=capture_session_id)

    nopl_img = capture_session.rawimage_set.filter(
        image_type=RawImage.NON_POLARIZED_FILTER,
    ).order_by("time_taken").all()

    pl_img = capture_session.rawimage_set.filter(
        image_type=RawImage.POLARIZED_FILTER
    ).order_by("time_taken").all()

    id_img = capture_session.rawimage_set.filter(
        image_type=RawImage.IDENTIFICATION
    ).order_by("time_taken").all()

    context = {
        "capture_session": capture_session,
        "nopl_img": nopl_img,
        "pl_img": pl_img,
        "id_img": id_img
    }

    return render_to_response("image_app/capture_session_detail.html", context,
                              context_instance=RequestContext(request))


def analysis_session_index(request):
    analysis_sessions = ImageAnalysisSession.objects.order_by("-date_created").all()
    if request.method == "POST":
        form = ImageAnalysisSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ia_analysis_session_index")
    else:
        form = ImageAnalysisSessionForm()

    context = {
        "analysis_sessions": analysis_sessions,
        "form": form
    }
    return render_to_response("image_app/analysis_session_index.html", context,
                              context_instance=RequestContext(request))


def analysis_session_detail(request, analysis_session_id):
    analysis_session = get_object_or_404(ImageAnalysisSession, pk=analysis_session_id)
    ia_parameters = analysis_session.imageanalysisparameter_set.all()
    ia_parameter_form = ImageAnalysisParameterForm()
    lst_analysis_cs_result = analysis_session.analysiscapturesessionresult_set.all()

    if request.method == "POST":
        ia_parameter_form = ImageAnalysisParameterForm(request.POST)
        if ia_parameter_form.is_valid():
            analysis_parameter = ia_parameter_form.save(commit=False)
            analysis_parameter.analysis_session = analysis_session
            analysis_parameter.save()
            return redirect("ia_analysis_session_detail", analysis_session_id=analysis_session_id)

    xdata = ["nightime image", "daytime image"]
    ydata = [ia_parameters.filter(capture_session__period=CaptureSession.NIGHT_IMAGE).count(),
             ia_parameters.filter(capture_session__period=CaptureSession.DAY_IMAGE).count()]

    color_list = ['#5d8aa8', '#e32636']

    extra_serie = {
        "tooltip": {"y_start": "", "y_end": " Capture Session"},
        "color_list": color_list
    }
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'  # container name

    piechart_data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }

    xdata = []
    for analysis_cs_result in lst_analysis_cs_result.all():
        raw_time = analysis_cs_result.analysis_parameter.capture_session.time_taken.timetuple()
        xdata.append(int(time.mktime(raw_time) * 1000))

    daytime_max_area = []
    nighttime_max_area = []

    cur_dt = None
    cur_nt = None
    for analysis_cs_result in lst_analysis_cs_result:
        if analysis_cs_result.analysis_parameter.capture_session.period == CaptureSession.DAY_IMAGE:
            if cur_nt is None:
                cur_nt = 0
            cur_dt = analysis_cs_result.pupil_max_area
            daytime_max_area.append(int(cur_dt))
            nighttime_max_area.append(0)
        else:
            if cur_dt is None:
                cur_dt = 0
            cur_nt = analysis_cs_result.pupil_max_area
            nighttime_max_area.append(int(cur_nt))
            daytime_max_area.append(0)

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie1 = {
        "tooltip": {"y_start": "max area ", "y_end": " in pixel"},
        "date_format": tooltip_date
    }
    chartdata = {'x': xdata,
                 'name1': 'Pupil daytime max area', 'y1': daytime_max_area, 'extra1': extra_serie1,
                 'name2': 'Pupil nighttime max area', 'y2': nighttime_max_area, 'extra2': extra_serie1}

    charttype = "multiBarChart"
    chartcontainer = 'multibarchart_container'  # container name

    linechart_data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d %b %Y %H',
            'tag_script_js': True,
            'jquery_on_ready': True,
        }
    }

    context = {
        "linechart_data": linechart_data,
        "piechart_data": piechart_data,
        "ia_parameter_form": ia_parameter_form,
        "analysis_session": analysis_session,
        "ia_parameters": ia_parameters,
        "lst_analysis_cs_result": lst_analysis_cs_result
    }

    return render_to_response("image_app/analysis_session_detail.html", context,
                              context_instance=RequestContext(request))

def update_analysis_result(analysis_session_id, analysis_param_id):
    analysis_session = ImageAnalysisSession.objects.get(pk=analysis_session_id)
    analysis_param = ImageAnalysisParameter.objects.get(pk=analysis_param_id)
    analysis_cs_result, created = AnalysisCaptureSessionResult.objects.get_or_create(
        analysis_session=analysis_session,
        analysis_parameter=analysis_param
    )

    lst_nopl_img = analysis_param.capture_session.rawimage_set.filter(
        image_type=RawImage.NON_POLARIZED_FILTER
    ).order_by("time_taken").all()

    max_area = None
    for nopl in lst_nopl_img:
        analysis_result = ImageAnalysisResult.objects.get(
            analysis_session=analysis_session,
            raw_image=nopl
        )
        if max_area is None:
            max_area = analysis_result.pupil_area
        else:
            if analysis_result.pupil_area is not None and max_area < analysis_result.pupil_area:
                max_area = analysis_result.pupil_area

    analysis_cs_result.pupil_max_area = max_area
    analysis_cs_result.save()

    for nopl in lst_nopl_img:
        analysis_result = ImageAnalysisResult.objects.get(
            analysis_session=analysis_session,
            raw_image=nopl
        )
        if analysis_result.pupil_area is not None:
            analysis_result.pupil_normalized_area = ellipse_normalized_area(analysis_result.pupil_area, max_area)
            analysis_result.pupil_ca = ellipse_calculate_ca(analysis_result.pupil_area, max_area)
            analysis_result.save()


def pupil_analysis_runner(request, analysis_session_id):
    analysis_session = get_object_or_404(ImageAnalysisSession, pk=analysis_session_id)

    lst_analysis_parameter = analysis_session.imageanalysisparameter_set.all()

    for param in lst_analysis_parameter:
        lst_nopl_image = param.capture_session.rawimage_set.filter(
            image_type=RawImage.NON_POLARIZED_FILTER
        ).order_by("time_taken").all()

        result_dir = os.path.join(
            settings.MEDIA_ROOT,
            settings.ANALYSIS_RESULT_FOLDER,
            analysis_session.name,
            param.capture_session.name
        )
        os.makedirs(result_dir, exist_ok=True)

        for nopl in lst_nopl_image:
            try:
                analysis_result, created = ImageAnalysisResult.objects.get_or_create(
                    analysis_session=analysis_session,
                    analysis_parameter=param,
                    raw_image=nopl
                )
                result_path = os.path.join(
                    result_dir,
                    "ar_"+nopl.name.split(".")[0] + ".png"
                )

                try:
                    bgr = cv2.imread(nopl.image_file.path, cv2.IMREAD_COLOR)
                    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
                    props, pupil_area = detect_pupil(rgb, param)
                    analysis_result.result_type = ImageAnalysisResult.PUPIL_DETECTED
                except ImpartialPupilDetected:
                    analysis_result.result_type = ImageAnalysisResult.IMPARTIAL_PUPIL_DETECTED
                except NoPupilDetected:
                    analysis_result.result_type = ImageAnalysisResult.NO_PUPIL_DETECTED

                if analysis_result.result_type is not ImageAnalysisResult.PUPIL_DETECTED:
                    analysis_result.save()
                else:
                    save_pupil_analysis_result(rgb, props, result_path)
                    analysis_result.img_result_path = result_path
                    analysis_result.pupil_eccentricity = props.eccentricity
                    analysis_result.pupil_area = props.filled_area
                    analysis_result.pupil_major_axis_length = props.major_axis_length
                    analysis_result.pupil_minor_axis_length = props.minor_axis_length
                    ellipse_analyser = EllipseAnalysis(
                        major_axis=props.major_axis_length,
                        minor_axis=props.minor_axis_length
                    )
                    analysis_result.pupil_perimeter = ellipse_analyser.calculate_perimeter()
                    analysis_result.pupil_ipr = ellipse_analyser.calculate_ipr()
                    analysis_result.save()

            except Exception as e:
                from IPython import embed
                embed()

        update_analysis_result(analysis_session_id, param.id)

    return redirect("ia_analysis_session_detail", analysis_session_id=analysis_session_id)

def analysis_result_detail(request, analysis_session_id, analysis_param_id):
    analysis_parameter = get_object_or_404(ImageAnalysisParameter, pk=analysis_param_id)
    analysis_session = get_object_or_404(ImageAnalysisSession, pk=analysis_session_id)

    lst_result = ImageAnalysisResult.objects.filter(
        analysis_session=analysis_session,
        analysis_parameter=analysis_parameter
    ).order_by("time_taken").all()

    context = {
        "analysis_session": analysis_session,
        "analysis_parameter": analysis_parameter,
        "lst_result": lst_result
    }

    return render_to_response("image_app/analysis_result_detail.html", context,
                              context_instance=RequestContext(request))
