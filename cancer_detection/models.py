from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    medical_record_number = models.CharField(max_length=50)

class MedicalImage(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='medical_images/')
    date_taken = models.DateField()

class GenomicData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    data = models.JSONField()

class CancerType(models.Model):
    name = models.CharField(max_length=100)
    stage = models.CharField(max_length=50)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
