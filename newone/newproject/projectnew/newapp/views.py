from django.shortcuts import render

from .models import Hello


# Create your views here.

def demo(request):
    obj=Hello.objects.all()
    return render(request, "index.html", {'result': obj})
