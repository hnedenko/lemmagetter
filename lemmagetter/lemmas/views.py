from django.shortcuts import render
from django.http import HttpResponse

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


def get_lemmas(request):
    lemmas = {
        'best': 'play',
        'running': 'Alex'
    }

    return lemmas
