# AICancerScreen/urls.py

from django.contrib import admin
from django.urls import path, include  # Include needed to connect app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cancer_detection.urls')),  # Include the app URLs
]
