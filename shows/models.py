import uuid
from django.db import models
from django.template.defaultfilters import slugify

class MediaBase(models.Model):
    """
    Abstract base class for all media types having a title,
    and thus a slug, complemented by a UUID
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=256, unique=True)


    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) if self.slug is None or self.slug == '' else self.slug
        return super(__class__, self).save(*args, **kwargs)


class Channel(MediaBase):
    """
    A media source, e.g. Hulu, Netflix, etc.
    """
    name = models.CharField(max_length=256, null=False, blank=False, unique=True)

    class Meta:
        abstract = False


class Show(MediaBase):
    """
    A 'Television' show, the top-level grouping of all the
    series/seasons/episodes
    """
    title = models.CharField(max_length=256, unique=True, null=False, blank=False)

    class Meta:
        abstract = False

class Series(MediaBase):
    """
    What the American viewing audience might call a Season, represents a grouping of Episodes within a show
    """
    show = models.ForeignKey(Show, related_name="shows", on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    channels = models.ManyToManyField(Channel, blank=True)

    class Meta:
        abstract = False
        unique_together = [['show', 'number']]

class Episode(MediaBase):
    """
    The actual thing you can watch, and its metadata
    """
    series = models.ForeignKey(Series, related_name="series", on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    video = models.URLField(null=False, blank=False)
    air_date = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=256, unique=True, null=False, blank=False)

    class Meta:
        abstract = False
        unique_together = [['series', 'number'],]

