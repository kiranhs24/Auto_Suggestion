import re

from elasticsearch import Elasticsearch
es_connection = Elasticsearch([{'host': 'localhost', 'port': '9200'}])


def build_autosuggest_query(q, limit=25):
    query = {
        "query":
            {
                "match_phrase_prefix": {
                    "word": q
                }
            },
        "size": limit
    }
    return query
