from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>/", views.monworkint),
    path("<str:month>/", views.monworkstr, name="int_month"),
    path("", views.months, name="index")
]