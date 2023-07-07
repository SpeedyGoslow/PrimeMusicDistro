from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("Tab",views.TAB,name="Tab"),
    path("LK/",views.LK,name="LK"),
    path("LP/",views.LP,name="LP"),
    path("SGS/",views.SGS,name="SGS"),
    path("TC/",views.TC,name="TC"),
    path("TL/",views.TL,name="TL"),
    path("JM/",views.JM,name="JM"),
    path("JT/",views.JT,name="JT"),
    path("MS/",views.MS,name="MS"),
]
