import csv
from elasticsearch.helpers import bulk
from auto_suggestion.Utils.utils import es_connection

words = {}


def index_record_to_elasticsearch(words):
        yield {
            "_index": "auto_suggestion",
            "_type": "_doc",
            "_source": words
        }


with open("word_search.tsv") as file:
    rd = csv.reader(file, delimiter="\t", quotechar='"')
    for row in rd:
        words['word'] = row[0]
        words['weight'] = row[1]
        bulk(es_connection, index_record_to_elasticsearch(words))
        print(words)
