from django.contrib import admin
from .models import Channel, Episode, Series, Show


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    pass


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    pass

