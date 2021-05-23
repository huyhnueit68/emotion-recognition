from django.contrib import admin
from .models import RequestImages, RequestClient
# Register your models here.

admin.site.register(RequestClient)
admin.site.register(RequestImages)
