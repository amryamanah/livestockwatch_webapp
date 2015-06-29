import os
from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.postgres.fields import HStoreField

from utils.model_util import ModelTimestamp


class CaptureSession(ModelTimestamp):
    NIGHT_IMAGE = 'nt'
    DAY_IMAGE = 'dt'
    PERIOD_TYPE = (
        (DAY_IMAGE, 'Day time image'),
        (NIGHT_IMAGE, 'Night time image'),
    )
    cattle = models.ForeignKey("core_app.Cattle")
    name = models.CharField(_("CS Name"), max_length=100, null=True)
    period = models.CharField(_("Day period"), max_length=2, choices=PERIOD_TYPE)
    folder_path = models.CharField(_("CS folder path"), max_length=300, null=True)
    time_taken = models.DateTimeField(_("CS time taken"), null=True)

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.cattle.id_number, self.name)

    def save(self, *args, **kwargs):
        self.folder_path = os.path.join(
            settings.MEDIA_ROOT,
            settings.CATTLE_IMAGE_FOLDER,
            self.cattle.id_number,
            self.name
        )
        super(CaptureSession, self).save(*args, **kwargs)

    class Meta:
        unique_together = ("cattle", "name")


def generate_filepath(self, filename):
    generated_filename = os.path.join(
        settings.CATTLE_IMAGE_FOLDER,
        self.capture_session.cattle.id_number,
        self.capture_session.name,
        filename
    )
    return generated_filename

class RawImage(ModelTimestamp):
    POLARIZED_FILTER = 'PL'
    NON_POLARIZED_FILTER = 'NOPL'
    IDENTIFICATION = 'ID'
    IMAGE_TYPE_CHOICES = (
        (POLARIZED_FILTER, 'Polarized Filter'),
        (NON_POLARIZED_FILTER, 'Non Polarized Filter'),
        (IDENTIFICATION, 'Identification'),
    )
    capture_session = models.ForeignKey(CaptureSession)
    name = models.CharField(_("RI name"), max_length=300)
    image_type = models.CharField(_("RI image type"), max_length=4, choices=IMAGE_TYPE_CHOICES)
    time_taken = models.DateTimeField(_("RI time taken"), null=True)
    image_file = models.FileField(_("RI image file"), upload_to=generate_filepath)

    class Meta:
        unique_together = ("name", "capture_session")

    def save(self, *args, **kwargs):
        if self.image_file:
            filename_part = self.image_file.name.split("_")
            raw_timetaken = '{}/{}/{} {}:{}:{}'.format(
                filename_part[1],
                filename_part[2],
                filename_part[3],
                filename_part[4],
                filename_part[5],
                ".".join([filename_part[6], filename_part[7]])
            )

            if raw_timetaken.endswith(".bmp"):
                raw_timetaken = raw_timetaken.split(".bmp")[0]

            image_type = filename_part[0]
            if image_type == "id":
                self.image_type = self.IDENTIFICATION
            elif image_type == "nopl":
                self.image_type = self.NON_POLARIZED_FILTER
            elif image_type == "pl":
                self.image_type = self.POLARIZED_FILTER

            self.name = self.image_file.name
            self.time_taken = datetime.strptime(raw_timetaken, '%Y/%m/%d %H:%M:%S.%f')

        super(RawImage, self).save(*args, **kwargs)

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.capture_session.id, self.name)

class ImageAnalysisSession(ModelTimestamp):
    FINISH = 2
    IN_PROGRESS = 1
    PENDING = 0
    ANALYSIS_STATE = (
        (FINISH, 'Finish'),
        (IN_PROGRESS, 'In Progress'),
        (PENDING, 'Pending'),
    )
    name = models.CharField(_("IAS name"), max_length=300)
    remarks = models.TextField(_("IAS remarks"), blank=True, null=True)
    analysis_state = models.IntegerField(_("IAS analysis state"),
                                         choices=ANALYSIS_STATE, default=PENDING)

    def __str__(self):
        return "{}: {}".format(self.id, self.name)

class ImageAnalysisParameter(ModelTimestamp):
    analysis_session = models.ForeignKey(ImageAnalysisSession)
    capture_session = models.ForeignKey(CaptureSession)
    hue_max = models.FloatField(_("Hue threshold max"), default=1.00)
    hue_min = models.FloatField(_("Hue threshold min"), default=0.00)
    sat_max = models.FloatField(_("Saturation threshold max"), default=1.00)
    sat_min = models.FloatField(_("Saturation threshold min"), default=0.00)
    val_max = models.FloatField(_("Value threshold max"), default=1.00)
    val_min = models.FloatField(_("Value threshold min"), default=0.00)

    class Meta:
        unique_together = ["analysis_session", "capture_session"]

class ImageAnalysisResult(ModelTimestamp):
    NO_PUPIL_DETECTED = 0
    IMPARTIAL_PUPIL_DETECTED = 1
    PUPIL_DETECTED = 2
    RESULT_TYPE = (
        (NO_PUPIL_DETECTED, 'No pupil detected'),
        (IMPARTIAL_PUPIL_DETECTED, 'Impartial pupil detected'),
        (PUPIL_DETECTED, 'Pupil detected'),
    )
    analysis_session = models.ForeignKey(ImageAnalysisSession)
    analysis_parameter = models.ForeignKey(ImageAnalysisParameter)
    raw_image = models.ForeignKey(RawImage)

    img_result_path = models.FilePathField(_("Image analysis result path"), null=True, recursive=True, max_length=300)
    result_type = models.IntegerField(_("IAR analysis state"),
                                      choices=RESULT_TYPE, null=True)
    # distance data
    pl_distance = models.FloatField(_("IAR pl distance"), null=True)
    nopl_distance = models.FloatField(_("IAR nopl distance"), null=True)

    # rgb data
    pupil_avg_red = models.FloatField(_("IAR pupil red channel average"), null=True)
    pupil_avg_green = models.FloatField(_("IAR pupil green channel average"), null=True)
    pupil_avg_blue = models.FloatField(_("IAR pupil blue channel average"), null=True)

    # shape data
    pupil_eccentricity = models.FloatField(_("IAR pupil eccentricity"), null=True)
    pupil_area = models.FloatField(_("IAR pupil area"), null=True)
    pupil_ca = models.FloatField(_("IAR constriction amplitude"), null=True)
    pupil_perimeter = models.FloatField(_("IAR pupil perimeter"), null=True)
    pupil_major_axis_length = models.FloatField(_("IAR pupil major axis length"), null=True)
    pupil_minor_axis_length = models.FloatField(_("IAR pupil minor axis length"), null=True)
    pupil_ipr = models.FloatField(_("IAR initial pupil roundness"), null=True)

    # capture_session data
    pupil_max_area = models.FloatField(_("IAR pupil max area"), null=True)
    pupil_normalized_area = models.FloatField(_("IAR pupil normalized area"), null=True)
    time_taken = models.DateTimeField(_("IAR time taken"), null=True)

    class Meta:
        unique_together = ("analysis_session", "raw_image")

    def save(self, *args, **kwargs):
        filename_part = self.raw_image.name.split("_")
        raw_timetaken = '{}/{}/{} {}:{}:{}'.format(
                filename_part[1],
                filename_part[2],
                filename_part[3],
                filename_part[4],
                filename_part[5],
                ".".join([filename_part[6], filename_part[7]])
            )

        if raw_timetaken.endswith(".bmp"):
            raw_timetaken = raw_timetaken.split(".bmp")[0]

        self.time_taken = datetime.strptime(raw_timetaken, '%Y/%m/%d %H:%M:%S.%f')
        if len(filename_part) > 8 and self.raw_image is not self.raw_image.IDENTIFICATION:
                self.nopl_distance = float(filename_part[8][4:][:-2])
                self.pl_distance = float(filename_part[9][2:][:-6])

        super(ImageAnalysisResult, self).save(*args, **kwargs)
