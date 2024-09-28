from django.contrib import admin
from .models import Patient, MedicalImage, GenomicData, CancerType

admin.site.register(Patient)
admin.site.register(MedicalImage)
admin.site.register(GenomicData)
admin.site.register(CancerType)
