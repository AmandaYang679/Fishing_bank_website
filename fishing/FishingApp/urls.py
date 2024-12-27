from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('authorization', views.authorization),
    path('login', views.login)

]