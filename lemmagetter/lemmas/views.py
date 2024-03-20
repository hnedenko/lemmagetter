from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

"""
def get_lemmas(words):
    import spacy
    nlp = spacy.load("en_core_web_sm")
    
    lemmas = dict()

    doc = nlp(" ".join(words))

    for token in doc:
        lemmas[token] = token.lemma_

    return lemmas
"""

class LemmasAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        print("Запрос GET принят!")
        return Response({'title': 'Круто! Метод GET работает!'})

    def post(self, request):
        print("Запрос POST принят!")
        return Response({'title': 'Круто! Метод POST работает!'})
