from django.urls import path
from . import views

urlpatterns = [
    path('',views.SWA,name="SWA"),
]
