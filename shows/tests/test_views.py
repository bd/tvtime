from django.test import TestCase
from django.test import Client
from model_mommy import mommy
from ..models import Episode


class TestViewsReachable(TestCase):

    def test_episode_show_returned(self):
        c = Client()
        epi = mommy.make(Episode)
        show_slug = 'bobs-burgers'
        epi.series.show.slug = 'bobs-burgers'
        epi.series.show.save()
        url = f'/shows/{show_slug}/rnd'
        response = c.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, epi.video)

