import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "TitanIA"
    API_V1_STR: str = "/api/v1"
    
    # Vector DB
    CHROMA_DB_DIR: str = "chroma_db"
    COLLECTION_NAME: str = "titania_docs"
    
    # AWS (Mock or Real)
    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID", "mock_key")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY", "mock_secret")
    AWS_REGION: str = os.getenv("AWS_REGION", "us-east-1")
    S3_BUCKET_NAME: str = os.getenv("S3_BUCKET_NAME", "titania-docs")
    USE_REAL_S3: bool = os.getenv("USE_REAL_S3", "False").lower() == "true"
    
    # AWS Bedrock
    USE_BEDROCK: bool = os.getenv("USE_BEDROCK", "False").lower() == "true"
    BEDROCK_REGION: str = os.getenv("BEDROCK_REGION", "us-east-1")
    BEDROCK_EMBEDDING_MODEL_ID: str = os.getenv("BEDROCK_EMBEDDING_MODEL_ID", "amazon.titan-embed-text-v1")
    BEDROCK_LLM_MODEL_ID: str = os.getenv("BEDROCK_LLM_MODEL_ID", "anthropic.claude-3-sonnet-20240229-v1:0")

    class Config:
        env_file = ".env"

settings = Settings()
