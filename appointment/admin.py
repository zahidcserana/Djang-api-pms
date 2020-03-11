from django.contrib import admin

from .models import AppointmentSerial, DoctorAppointment

admin.site.register(AppointmentSerial)
admin.site.register(DoctorAppointment)
