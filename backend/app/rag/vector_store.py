import os
from typing import List
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.embeddings import BedrockEmbeddings
from langchain_core.documents import Document
from app.core.config import settings

class VectorStore:
    def __init__(self):
        if settings.USE_BEDROCK:
            self.embedding_function = BedrockEmbeddings(
                client=None, # Boto3 client will be created automatically if credentials are in env
                region_name=settings.BEDROCK_REGION,
                model_id=settings.BEDROCK_EMBEDDING_MODEL_ID
            )
        else:
            self.embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            
        self.persist_directory = settings.CHROMA_DB_DIR
        
        self.db = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embedding_function,
            collection_name=settings.COLLECTION_NAME
        )


    def similarity_search(self, query: str, k: int = 4) -> List[Document]:
        """
        Search for similar documents.
        """
        return self.db.similarity_search(query, k=k)
