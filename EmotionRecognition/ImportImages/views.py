from django.shortcuts import render
from django.http import HttpResponse
from .models import RequestClient
from .models import RequestImages


# Create your views here.

def index(request):
    return render(request, "ImportImages/index.html")


def viewResultClient(request, request_id):
    resultClient = RequestClient.objects.get(pk=request_id)
    content = {"resultClient": resultClient}
    return render(request, "ImportImages/resultRequest.html", content)
