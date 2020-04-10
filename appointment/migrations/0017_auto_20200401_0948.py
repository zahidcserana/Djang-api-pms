# Generated by Django 3.0.2 on 2020-04-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0016_doctorappointment_problem'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorappointment',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctorappointment',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='MALE', max_length=10),
        ),
    ]