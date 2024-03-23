from django.test import TestCase
from . import views
from rest_framework.test import APIClient, APITestCase
from rest_framework.request import Request


class TestsGetLemmas(APITestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_lemmas_status(self):
        words = ["best", "running"]
        correct_lemmas = {'best': 'good', 'running': 'run'}

        client = APIClient()
        response = self.client.post(views.LemmasAPIView.as_view(), {'words': words})
        response.render()

        self.assertEqual(200, response.status_code)

"""
    def test_get_lemmas_data(self):
        words = ["best", "running"]
        correct_lemmas = {'best': 'good', 'running': 'run'}

        client = APIClient()
        response = client.post(views.LemmasAPIView.as_view(), {'words': words})
        response.render()

        self.assertEqual(correct_lemmas, response)
"""
