from django.shortcuts import render

import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

import spacy


class LemmasAPIView(APIView):

    def initial(self, request, *args, **kwargs):
        permission_classes = [AllowAny]

    def post(self, request):

        # get input words from request body
        words = json.loads(request.data['words'])

        # analyze words: get lemmas
        nlp = spacy.load("en_core_web_sm")
        lemmas = dict()
        lemmas['lemmas'] = dict()
        doc = nlp(" ".join(words))
        for token in doc:
            lemmas['lemmas'][str(token)] = token.lemma_

        return Response(lemmas, 200)
