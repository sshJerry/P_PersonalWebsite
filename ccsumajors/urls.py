from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_index, name="index"),
    path('degree', views.view_degree, name="degree"),
    path('project', views.view_project, name='project'),
    path('login', views.view_login, name="login"),
    path('register', views.view_register, name='register'),
    path('logout', views.view_logout, name='logout'),
]
