import requests
import json
import elasticsearch


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
                        "fuzziness": 2
                    }
                }
            }
        }
    }
    # payload = json.dumps(payload)
    results = es.search(index=index, body=query)
    suggestions = results["suggest"]["title-suggest"][0]["options"]
    titles = []
    for suggestion in suggestions:
        print("sugestioins >>>>>>>>>>>>>>>>>>>>>", suggestion["text"])
        titles.append(suggestion['text'])
    # if response.status_code == 200:
    #     response = json.loads(response.text)
    #     print("response :::::::", response)
    #     options = response["suggest"]["movie-suggest"][0]["options"]
    #     search_id = 1
    #     for option in options:
    #         titles.append(
    #             {
    #                 "id": search_id,
    #                 "value": option["text"]
    #             }
    #         )
    #         search_id += 1
    return titles


def string_query_search(query):
    query = {
        "query": {
            "query_string": {
                "analyze_wildcard": True,
                "query": query,
                "fields": ["title", "desc"]
            }
        },
        "size": 10
    }
    res = []
    results = es.search(index=index, body=query)
    for hit in results["hits"]["hits"]:
        print(hit["_source"])
        res.append(hit["_source"])
    return res
