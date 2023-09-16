from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from account.sendmail import send_mail

class UserSerializer (ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {
                "write_only":True,
                "required" : True 

            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_active = False
        user.save()
        send_mail(user.email, "Account confirmation" , "Your account was succesfully created")
        return user