# Generated by Django 3.0.2 on 2020-03-27 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_appointmentserial_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorappointment',
            name='mobile',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctorappointment',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]