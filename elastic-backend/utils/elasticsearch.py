from pathlib import Path
import elasticsearch
from elasticsearch.helpers import bulk
import requests
import json
import csv


class Elasticsearch:
    def __init__(self, index):
        self.index = index
        self.es = elasticsearch.Elasticsearch(["http://localhost:9200"])
        self.headers = {
            'Content-Type': 'application/json'
        }

    def es_healthcheck(self):
        try:
            response = self.es.cluster.health()
            if (response):
                status = response["status"]
                if (status != "red"):
                    print("💪 ES is {} and healthy".format(status))
                    return True
                else:
                    print("🤒 ES is {} and not healthy".format(status))
                    return False
            else:
                return False
        except Exception as e:
            print("❌ Exception: ", e)
            return False

    def create_es_index(self):
        print(self.index)
        # Create ES template and index if not exist
        for index in self.es.indices.get('*'):
            print("index>>>>>>>>>>>>>>>>>>>>>", index)
        try:
            mapping_custom = {
                "settings": {
                    "number_of_shards": 1,
                    "number_of_replicas": 0
                },
                "mappings": {
                    "properties": {
                        "title": {
                            "type": "completion"
                        },
                        "year": {
                            "type": "text"
                        },
                        "certificate": {
                            "type": "text"
                        },
                        "duration": {
                            "type": "text"
                        },
                        "genre": {
                            "type": "text"
                        },
                        "desc": {
                            "type": "text"
                        },
                        "rating": {
                            "type": "text"
                        },
                        "votes": {
                            "type": "text"
                        }
                    }
                }
            }
            self.es.indices.create(
                index=self.index, body=mapping_custom)
        except Exception as e:
          print('An exception occurred', e)

    def add_documents(self, filepath):
        buld_data = []

        with open(filepath, 'r') as csvfile:
            movie_reader = csv.DictReader(csvfile)
            i = 0
            for row in movie_reader:
                title = row['title']
                year = row['year']
                certificate = row['certificate']
                duration = row['runtime']
                genre = row['genre']
                desc = row['desc']
                rating = row['rating']
                votes = row['votes']
                buld_data.append({
                    "_index": self.index,
                    "_id": i,
                    "_source": {
                        'title': title,
                        'year': year,
                        'certificate': certificate,
                        'duration': duration,
                        'genre': genre,
                        'desc': desc,
                        'rating': rating,
                        'votes': votes
                    }
                })
                i += 1

        res = bulk(self.es, buld_data)
        print(res)

    def es_record_count(self):
        pass

    # def pre_condition_check(self):
    #     if (self.es_healthcheck()):
    #         self.create_es_index()
    #         self.add_documents()
    #         total_doc = self.es_record_count()
    #         if (total_doc > 0):
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False
