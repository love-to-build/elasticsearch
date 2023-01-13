import elasticsearch
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.filters import autocomplete_helper, string_query_search

from utils.elasticsearch import Elasticsearch


app = FastAPI()

origins = [
    "*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

est = Elasticsearch("movies")
est.create_es_index()
# est.add_documents("./movies.csv")


@app.get("/autocomplete")
def autocomplete(query: str = ""):
    result = autocomplete_helper(query)
    return result


@app.get("/string-query-search")
async def string_query_seach(query: str = ""):
    if (est.es_healthcheck):
        result = string_query_search(query)
        return result
    else:
        return []

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    """_summary_
    """
