from django.contrib import admin
from .models import Channel, Episode, Series, Show

# Register your models here.
admin.site.register(Channel)
admin.site.register(Episode)
admin.site.register(Series)
admin.site.register(Show)
