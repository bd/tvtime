from django.test import TestCase

from ..models import Show

class AutoSlugMixinTestCase(TestCase):

    def test_save_creates_slug(self):
        howdy_doody = Show.objects.create(title="Howdy Doody's Fun-time Hour!")
        self.assertEqual(howdy_doody.slug, "howdy-doodys-fun-time-hour")

    def test_no_slug_overwrite_on_save(self):
        show = Show.objects.create(title="Love Boat")
        self.assertEqual(show.slug, 'love-boat')
        show.title = 'Love Vessel'
        self.assertEqual(show.slug, 'love-boat')

    def test_uuid_mixin(self):
        my_show = Show.objects.create(title="Twighlight Zone")
        self.assertIsNotNone(my_show.id)
        self.assertEqual(len(my_show.id.bytes), 16)


