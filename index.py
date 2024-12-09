from llama_index.core import GPTVectorStoreIndex, VectorStoreIndex, StorageContext, Document
import openai
import json

openai.api_key = "my-api-key"

with open("dataset.json", "r", encoding = "utf-8") as f:
  data = json.load(f)

documents = [Document(text=item["content"], metadata={"filename": item["filename"]}) for item in data]

storage_context = StorageContext.from_defaults()
index = GPTVectorStoreIndex.from_documents(documents, storage_context=storage_context)

index.storage_context.persist("vectorindex.json")

print("Index created and saved to disk")


