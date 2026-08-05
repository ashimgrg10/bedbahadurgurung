from django.test import SimpleTestCase
from django.urls import reverse


class JourneyViewTests(SimpleTestCase):
    def test_journey_view_includes_slider_images(self):
        response = self.client.get(reverse('portfolio:journey'))

        self.assertEqual(response.status_code, 200)
        self.assertIn('slider_images', response.context)
        self.assertGreaterEqual(len(response.context['slider_images']), 3)
