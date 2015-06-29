from django.contrib import admin

from .models import ImageAnalysisResult, ImageAnalysisSession, \
    RawImage, CaptureSession,ImageAnalysisParameter


admin.site.register(ImageAnalysisSession)
admin.site.register(RawImage)
admin.site.register(CaptureSession)
admin.site.register(ImageAnalysisResult)
admin.site.register(ImageAnalysisParameter)

