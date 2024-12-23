
from django.urls import path
from .views import  PostingOffert

urlpatterns = [
    path("post/", PostingOffert.as_view()),
]
