from .models import AppointmentSerial, DoctorAppointment
from rest_framework import serializers
from patient.serializers import PatientSerializer
from doctor.serializers import DoctorSerializer


class AppointmentSerialSerializer(serializers.HyperlinkedModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    doctor_id = serializers.IntegerField()

    class Meta:
        model = AppointmentSerial
        fields = ['id', 'schedule_time', 'name', 'mobile', 'doctor', 'doctor_id', 'status', 'created_at']


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension,)
            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class DoctorAppointmentSerializer(serializers.HyperlinkedModelSerializer):
    patient = PatientSerializer(read_only=True)
    patient_id = serializers.IntegerField()
    doctor = DoctorSerializer(read_only=True)
    doctor_id = serializers.IntegerField()
    doc_image = Base64ImageField(
        allow_null=True, max_length=None, use_url=True, required=False
    )
    doc_file = Base64ImageField(
        allow_null=True, max_length=None, use_url=True, required=False
    )

    class Meta:
        model = DoctorAppointment
        fields = ['id', 'name', 'mobile', 'problem', 'age', 'gender', 'description', 'doctor', 'doctor_id', 'patient',
                  'patient_id', 'advice', 'doc_image', 'doc_file', 'created_at']
