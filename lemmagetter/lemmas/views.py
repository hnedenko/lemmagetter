import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

import spacy


class LemmasAPIView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nlp = spacy.load("en_core_web_sm")

    def initial(self, request, *args, **kwargs):
        permission_classes = [AllowAny]

    def post(self, request):

        # get input words from request body
        words = json.loads(request.data['words'])

        # analyze words: get lemmas
        lemmas = dict()
        lemmas['lemmas'] = dict()
        doc = self.nlp(" ".join(words))
        for token in doc:
            lemmas['lemmas'][str(token)] = token.lemma_

        return Response(lemmas, 200)
