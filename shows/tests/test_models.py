from django.test import TestCase

from ..models import Show

class AutoSlugMixinTestCase(TestCase):

    def test_save_creates_slug(self):
        howdy_doody = Show.objects.create(title="Howdy Doody's Fun-time Hour!")
        self.assertEqual(howdy_doody.slug, "howdy-doodys-fun-time-hour")

    def test_no_slug_overwrite_on_save(self):
        howdy_doody = Show.objects.create(title="Love Boat")
        self.assertEqual(howdy_doody.slug, 'love-boat')
        howdy_doody.title = 'Love Vessel'
        self.assertEqual(howdy_doody.slug, 'love-boat')


