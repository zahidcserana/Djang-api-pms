from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

# from .models import User
from rest_framework import serializers
from rest_framework_jwt.serializers import User

from setting.serializers import DepartmentSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # department = DepartmentSerializer(read_only=True)
    # department_id = serializers.IntegerField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        # fields = ['id', 'name', 'department', 'department_id', 'email', 'mobile', 'type', 'status', 'timestamp']

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.mobile = validated_data.get('mobile', instance.mobile)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.type = validated_data.get('type', instance.type)
    #     instance.department_id = validated_data.get('department_id', instance.department_id)
    #
    #     instance.save()
    #     return instance


class UserRegistrationSerializer(ModelSerializer):
    def validate(self, data):
        # if self.initial_data['mobile'][0] == '+':
        #     # remove country code for now
        #     self.initial_data['mobile'] = self.initial_data['mobile'][3:]
        # elif self.initial_data['mobile'][0] == '8':
        #     # remove partial country code for now
        #     self.initial_data['mobile'] = self.initial_data['mobile'][2:]
        # elif self.initial_data['mobile'][0] != '0':
        #     # add a zero at the beginning
        #     # only if someone forgot to write as 01712....
        #     self.initial_data['mobile'] = '0{}'.format(self.initial_data['mobile'])
        return data

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.set_password(self.initial_data['password'])
        instance.is_active = True
        instance.save()
        return instance

    # # send OTP
    # secret = pyotp.random_base32()
    # hotp = pyotp.HOTP(secret)
    # otp_string = hotp.at(0)
    #
    # # create OTP object in DB
    # OTP.objects.create(
    #     counter=0,
    #     otp=otp_string,
    #     secret=secret,
    #     user=instance
    # )

    # for testing, skip the SMS and Email sending
    # if 'test' not in sys.argv:
    #     # send OTP via SMS
    #     send_sms.delay(
    #         '+88{}'.format(serializer.data['mobile']),
    #         "Your OTP for Subidha is {}".format(otp_string)
    #     )

    # # send activation mail
    # send_email.delay(
    #     instance.email,
    #     'Activate Your Account',
    #     render_to_string('email/index.html', {
    #         'link': '{}api/v1/user/email/activate/{}/'.format(
    #             settings.BASE_URL,
    #             instance.alias
    #         )
    #     })
    # )
    #
    # return instance

    class Meta:
        model = User

        fields = (
            # 'alias',
            # 'mobile',
            'username',
            'email',
            'password',
            # 'occupation',
            # 'address_one',
            # 'address_two',
            # 'dob',
            # 'gender',
        )
        # read_only_fields = (
        #     'email',
        # )
