# LlamaIndex_Proj

Searchable Resume Doc Repository

This project demonstrates how to create, store and query a vector-based index for semantic search. This project uses a dataset of Resumes found on Kaggle https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset?resource=download.

Features:
- Load a dataset from pdf format to txt to JSON
- Converted the JSON data file into a semantic vector index
- Saved the semantic vector index to disk for efficent reuse
- Utilizes OpenAI embedding model

Prerequisites
- Python 3.8 or higher
- Open API key

Libraries
- pip install llama-index openai python-dotenv

Setup
- git clone https://github.com/edw7777/LlamaIndex_Proj.git
- cd LlamaIndex_Proj
- Input your OpenAI key where it says "insert-api-key"
- Add your dataset of pdfs

Usage
- python index.py
- python query.py, it will prompt you to insert a query
