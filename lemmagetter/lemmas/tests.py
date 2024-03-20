from django.test import TestCase
from . import views
from rest_framework.test import APIClient


class TestsGetLemmas(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_lemmas_status(self):
        words = ["best", "running"]
        correct_lemmas = {'best': 'good', 'running': 'run'}

        client = APIClient()
        response = client.post(views.LemmasAPIView.as_view(), {'data': words})

        self.assertEqual(response.status_code, 200)

    def test_get_lemmas_data(self):
        words = ["best", "running"]
        correct_lemmas = {'best': 'good', 'running': 'run'}

        client = APIClient()
        response = client.post(views.LemmasAPIView.as_view(), {'data': words})

        self.assertEqual(correct_lemmas, 12)
