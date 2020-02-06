from django.db import models


class Show(models.Model):
    """
    A 'Television' show, the top-level grouping of all the
    series/seasons/episodes
    """
    pass

class Series(models.Model):
    """
    What the American viewing audience might call a Season, represents a grouping of Episodes within a show
    """
    pass

class Episode(models.Model):
    """
    The actual thing you can watch, and its metadata
    """
    pass