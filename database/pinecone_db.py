import logging
from typing import List

import pinecone
from icecream import ic
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document
from langchain.vectorstores import Pinecone

from constants import PINECONE_API_KEY, PINECONE_API_ENV, INDEX_NAME


# @cache
def index_list() -> List[str]:
    return pinecone.list_indexes()


def create_index(index_name: str = INDEX_NAME, dimension: int = 1536, metric: str = "euclidean"):
    # check before creating
    if index_name not in index_list():
        # index not existed. Create a new index
        pinecone.create_index(name=index_name, dimension=dimension, metric=metric)
        ic(f"create a new index {index_name}")
    else:
        logging.warning(f"{index_name} index existed. skip creating.")


def insert(data: List[Document], embeddings: OpenAIEmbeddings, index=INDEX_NAME) -> Pinecone:
    return Pinecone.from_documents(data, embedding=embeddings, index_name=index)

# class PineconeDB:
#     __slots__ = []  # Perf: debug
#
#     def __init__(self):
#         pinecone.init(
#             api_key=PINECONE_API_KEY,
#             environment=PINECONE_API_ENV,
#         )
#
#     @property
#     @cache
#     def index_list(self,cached:int=0): #use any other number to get the latest
#         return pinecone.list_indexes()
