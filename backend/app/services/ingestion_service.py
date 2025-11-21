import os
from fastapi import UploadFile
from app.ingestion.s3_connector import S3Connector
from app.ingestion.loaders import DocumentLoader
from app.ingestion.chunker import TextChunker
from app.rag.vector_store import VectorStore

class IngestionService:
    def __init__(self):
        self.s3 = S3Connector()
        self.loader = DocumentLoader()
        self.chunker = TextChunker()
        self.vector_store = VectorStore()

    async def process_document(self, file: UploadFile):
        # 1. Upload to S3 (Mock)
        file_path = await self.s3.upload_file(file)
        
        # 2. Load Document
        documents = self.loader.load_file(file_path)
        
        # 3. Chunk Document
        chunks = self.chunker.split_documents(documents)
        
        # 4. Index in Vector DB
        self.vector_store.add_documents(chunks)
        
        return {
            "filename": file.filename,
            "s3_path": file_path,
            "num_chunks": len(chunks),
            "status": "indexed"
        }
