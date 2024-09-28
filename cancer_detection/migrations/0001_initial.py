# Generated by Django 5.1.1 on 2024-09-28 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('medical_record_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='medical_images/')),
                ('date_taken', models.DateField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cancer_detection.patient')),
            ],
        ),
        migrations.CreateModel(
            name='GenomicData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cancer_detection.patient')),
            ],
        ),
        migrations.CreateModel(
            name='CancerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('stage', models.CharField(max_length=50)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cancer_detection.patient')),
            ],
        ),
    ]
