from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core.retrievers import VectorIndexRetriever
import openai

openai.api_key = "my-api-key"

storage_context = StorageContext.from_defaults(persist_dir = "vectorindex.json")
index_new = load_index_from_storage(storage_context)

retriever = VectorIndexRetriever(index = index_new, similarity_top_k=5)

query_engine = index_new.as_query_engine()

response = query_engine.query(input("Enter your query"))

print(response)