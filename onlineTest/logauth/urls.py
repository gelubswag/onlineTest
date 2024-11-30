from django.urls import path
from logauth.views import *
app_name = "logauth"

urlpatterns = [
    path("", log, name="log"),
    path("/logout",logaut, name="logaut")
]