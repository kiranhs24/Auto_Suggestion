from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from auto_suggestion.Utils.utils import build_autosuggest_query, es_connection


class AutoSuggest(APIView):
    """
    """

    def get(self, request, format=None):
        """
        """
        q = request.GET.get('word')
        query = build_autosuggest_query(q)
        response = es_connection.search(index='auto_suggestion', body=query)

        suggestion = []

        for word in response['hits']['hits']:
            suggestion.append(word.get('_source'))
        return Response({"data": suggestion}, status=status.HTTP_200_OK)
