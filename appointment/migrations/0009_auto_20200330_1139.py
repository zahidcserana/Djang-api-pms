# Generated by Django 3.0.2 on 2020-03-30 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0008_auto_20200330_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorappointment',
            name='doc_file',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='doctorappointment',
            name='doc_image',
            field=models.FileField(upload_to=''),
        ),
    ]
