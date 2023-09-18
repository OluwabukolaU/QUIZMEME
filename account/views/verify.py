from django.http import HttpResponse
from ..models import Verification
from django.contrib.auth.models import User

def verify(request, pk, token):
    user = User.objects.get(pk=pk)
    verification = Verification.objects.get(user=user)
    if verification.token == token:
        if user.is_active:
            return HttpResponse("User already verified")
        user.is_active = True
        user.save()
        return HttpResponse("User verified")
    else:
        return HttpResponse("Invalid token")