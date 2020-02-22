from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from .models import Show

# Create your views here.
class RandomEpisodeView(SingleObjectMixin, View):
    model = Show

    def get(self, request, *args, **kwargs):
        self.show = self.get_object()
        episode = self.show.get_random_episode()
        return redirect(episode.video)


