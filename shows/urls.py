from django.urls import path

from . import views

urlpatterns = [
    path('<str:slug>/rnd', views.RandomEpisodeView.as_view())
]