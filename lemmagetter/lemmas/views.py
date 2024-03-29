import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from datetime import datetime

import spacy

# import logging


class LemmasAPIView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nlp = spacy.load("en_core_web_sm")
        # self.logger = logging.getLogger()

    def initial(self, request, *args, **kwargs):
        permission_classes = [AllowAny]

    def post(self, request):
        start_time = datetime.now()

        # get input words from request body
        words = json.loads(request.data['words'])

        # analyze words: get lemmas
        lemmas = dict()
        lemmas['lemmas'] = dict()
        doc = self.nlp(" ".join(words))
        for token in doc:
            lemmas['lemmas'][str(token)] = token.lemma_

        """
        # save log about request to DB
        self.logger.info({'request': request.data,
                          'response': lemmas,
                          'timestamp': start_time,
                          'duration': datetime.now() - start_time})
        """

        return Response(lemmas, 200)
