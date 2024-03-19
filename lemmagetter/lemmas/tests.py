from django.test import TestCase
from . import views


class TestsGetLemmas(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_correct_get_lemmas(self):
        words = ["best", "running"]
        correct_lemmas = {'best': 'good', 'running': 'run'}
        lemmas = views.get_lemmas(words)
        self.assertEqual(correct_lemmas, lemmas)
