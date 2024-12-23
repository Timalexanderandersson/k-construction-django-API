
from django.urls import path
from .views import PostOffert

urlpatterns = [
    path("posting/", PostOffert.as_view()),
]
