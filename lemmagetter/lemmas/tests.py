from django.test import TestCase, Client
from rest_framework.test import APITestCase


class TestsGetLemmas(APITestCase):

    def setUp(self):
        self.client = Client()
        self.url_getalllemmas = 'http://127.0.0.1:8000/lemmas/api/v1/getalllemmas'

    def tearDown(self):
        pass

    def test_get_lemmas_status(self):
        request = {"words": '["best", "running"]'}
        expected_response = {"lemmas": {"best": "good", "running": "run"}}

        response = self.client.post(self.url_getalllemmas, data=request)

        self.assertEqual(200, response.status_code)

    def test_get_lemmas_data(self):
        request = {"words": '["best", "running"]'}
        expected_response = {"lemmas": {"best": "good", "running": "run"}}

        response = self.client.post(self.url_getalllemmas, data=request)

        self.assertEqual(expected_response, response.data)
