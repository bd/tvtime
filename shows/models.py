from django.db import models
from django.template.defaultfilters import slugify

class AutoSlugModelMixin(models.Model):
    """
    Mixin to automatically create a slug given a title
    """
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) if self.slug is None or self.slug == '' else self.slug
        return super(__class__, self).save(*args, **kwargs)



class Show(AutoSlugModelMixin):
    """
    A 'Television' show, the top-level grouping of all the
    series/seasons/episodes
    """
    title = models.CharField(max_length=256, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=256, unique=True, null=False, blank=False)

class Series(AutoSlugModelMixin):
    """
    What the American viewing audience might call a Season, represents a grouping of Episodes within a show
    """
    pass

class Episode(AutoSlugModelMixin):
    """
    The actual thing you can watch, and its metadata
    """
    pass