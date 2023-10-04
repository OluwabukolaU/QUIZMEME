from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from account.sendmail import send_verification
from .models import Verification

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
        domain = self.context['request'].META['HTTP_HOST']
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        user.is_active = False
        user.save()
        Verification.objects.create(user=user)
        send_verification(user, domain)
        return user