from django.urls import path
from . import views

urlpatterns = [
    path('resultClient/<int:request_id>', views.viewResultClient, name='result'),
    path('', views.index, name="index"),
]
