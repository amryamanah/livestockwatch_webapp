from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from utils.model_util import ModelTimestamp

from farm_app.models import Stall


class Device(ModelTimestamp):
    stall = models.OneToOneField(Stall)
    name = models.CharField(_("Name"), max_length=20, unique=True)

    def __str__(self):
        return self.name


class DeviceError(ModelTimestamp):
    WARNING = 0
    CRITICAL = 1
    ERROR_SEVERITY = (
        (CRITICAL, 'Critical error'),
        (WARNING, 'Warning'),
    )
    CAMERA = 0
    ADDA = 1
    NETWORK = 2
    COMPONENT_TYPE =(
        (CAMERA, "Camera"),
        (ADDA, "ADDA board"),
        (NETWORK, "Network"),
    )
    UNRESOLVED = 0
    RESOLVED = 1
    STATUS_TYPE = (
        (RESOLVED, "Resolved"),
        (UNRESOLVED, "Unresolved"),
    )

    device = models.ForeignKey(Device)
    severity = models.IntegerField(_("Severity"), choices=ERROR_SEVERITY, null=True)
    component = models.IntegerField(_("Component"), choices=COMPONENT_TYPE, null=True)
    status = models.IntegerField(_("Status"), choices=STATUS_TYPE, default=UNRESOLVED)
    message = models.TextField(_("Message"), null=True)
    time_taken = models.DateTimeField(_("Time taken"), default=timezone.now)

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.device.name, self.message)


class DeviceCondition(ModelTimestamp):
    device = models.ForeignKey(Device)
    cpu_usage = models.FloatField(_("Cpu usage"), null=True)
    disk_usage = models.FloatField(_("Disk usage"), null=True)
    memory_usage = models.FloatField(_("Memory usage"), null=True)
    time_taken = models.DateTimeField(_("Time taken"), default=timezone.now)

    class Meta:
        unique_together = ("device", "time_taken")



class DeviceLog(ModelTimestamp):
    device = models.ForeignKey(Device)
    name = models.CharField(_("Name"), max_length=200)
    remarks = models.TextField(_("Remarks"), null=True)
    time_taken = models.DateTimeField(_("Time taken"), default=timezone.now)

    class Meta:
        unique_together = ("device", "time_taken")

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.device.name, self.name)
