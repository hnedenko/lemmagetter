from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

import spacy


class LemmasAPIView(APIView):

    def initial(self, request, *args, **kwargs):
        permission_classes = [AllowAny]

    def post(self, request):

        # split input str to world list
        words = request.data['words'].replace(',', '').split()

        # analyze words: get lemmas
        nlp = spacy.load("en_core_web_sm")
        lemmas = dict()
        doc = nlp(" ".join(words))
        for token in doc:
            lemmas[str(token)] = token.lemma_

        return Response(lemmas, 200)
