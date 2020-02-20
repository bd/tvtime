from django.test import TestCase
from django.test import Client
from model_mommy import mommy
from ..models import Episode

class TestViewsReachable(TestCase):

    def test_episode_show_returned(self):
        c = Client()
        epi = mommy.make(Episode)
        show_slug = epi.series.show.slug
        response = c.get(f'/shows/{show_slug}/rnd/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response.content, epi.video)