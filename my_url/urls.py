from django.contrib import admin
from django.urls import path, include
from .views import LinksView

urlpatterns = [
    path('api/<str:url>', LinksView.as_view()),
    path('api', LinksView.as_view())
]