# Generated by Django 3.0.2 on 2020-03-30 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0011_auto_20200330_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorappointment',
            name='doc_image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
