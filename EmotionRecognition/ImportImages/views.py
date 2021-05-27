from django.shortcuts import render
from django.http import HttpResponse
from .models import RequestClient
from .models import RequestImages
from datetime import date
from django.core.files.base import ContentFile
import os


# Create your views here.

def index(request):
    return render(request, "ImportImages/index.html")


def resultClient(request):
    return render(request, "ImportImages/resultRequest.html")
