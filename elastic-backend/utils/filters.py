import json
import elasticsearch
import requests

index = "movies"
es = elasticsearch.Elasticsearch(["http://localhost:9200"])
headers = {
    'Content-Type': 'application/json'
}


def autocomplete_helper(query):
    query = {
        "suggest": {
            "title-suggest": {
                "prefix": query,
                "completion": {
                    "field": "title",
                    "fuzzy": {
                        "fuzziness": 4,
                    }
                }
            }
        }
    }

    # payload = json.dumps(payload)
    results = es.search(index=index, body=query)
    suggestions = results["suggest"]["title-suggest"][0]["options"]
    titles = []
    i = 1
    for suggestion in suggestions:
        temp = {}
        temp['label'] = suggestion["text"]
        temp['value'] = suggestion['_id']
        titles.append(temp)

    return titles


def string_query_search(query):
    query = {
        "query": {
            "query_string": {
                "analyze_wildcard": True,
                "query": query,
                "fields": ["title", "genre", "desc"]
            }
        },
        "size": 10
    }
    res = []
    results = es.search(index=index, body=query)
    for hit in results["hits"]["hits"]:
        res.append(hit["_source"])
    return res
