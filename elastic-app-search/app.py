import json
from elastic_app_search import Client as ElasticClient


API_ENDPOINT = ""
API_KEY = ""
ENGINE_NAME=""

elastic_client = ElasticClient(base_endpoint=API_ENDPOINT, api_key=API_KEY)

file = open("./test.json")
data = json.load(file)

elastic_client.index_documents(engine_name=ENGINE_NAME, documents=data)