from django.urls import path
from .views import *

app_name="prima_app"
urlpatterns=[
  path("",indice,name="indice")
]