# Generated by Django 3.0.2 on 2020-03-30 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0009_auto_20200330_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorappointment',
            name='doc_file',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='doctorappointment',
            name='doc_image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
