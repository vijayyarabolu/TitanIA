import os
from typing import List
from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain_core.documents import Document

class DocumentLoader:
    @staticmethod
    def load_file(file_path: str) -> List[Document]:
        """
        Load a file based on its extension and return a list of Documents.
        """
        ext = os.path.splitext(file_path)[1].lower()
        
        if ext == ".pdf":
            loader = PyPDFLoader(file_path)
            return loader.load()
        elif ext == ".txt":
            loader = TextLoader(file_path)
            return loader.load()
        elif ext == ".csv":
            loader = CSVLoader(file_path)
            return loader.load()
        else:
            raise ValueError(f"Unsupported file type: {ext}")
