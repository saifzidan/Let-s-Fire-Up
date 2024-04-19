from django.urls import path
from . import views
app_name = "collect"
urlpatterns = [
    path("", views.index.as_view(), name="index"),
]
