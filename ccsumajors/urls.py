from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_index, name="index"),
    path('degree', views.view_degree, name="degree"),

]