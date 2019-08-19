from django.views.generic import TemplateView
from django.shortcuts import render


def IndexView(request):
    return render(request,'index.html')
