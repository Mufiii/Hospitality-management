from django.urls import path
from . import views

urlpatterns = [
    path("",views.index , name="home"),
    path("about",views.about, name='about'),
    path("booking",views.booking, name='booking'),
    path("doctor",views.doctor, name='doctors'),
    path("contact",views.contact, name='contacts'),
    path("department",views.department, name='departments'),
]

