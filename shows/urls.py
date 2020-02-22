from django.urls import path

from .views import RandomEpisodeView


urlpatterns = [
    path('<slug>/rnd', RandomEpisodeView.as_view(), name="random"),
]
