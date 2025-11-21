from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.rag_service import RAGService

router = APIRouter()
rag_service = RAGService()

class QueryRequest(BaseModel):
    query: str

@router.post("/query", summary="Retrieve context for a query")
def query_rag(request: QueryRequest):
    """
    Performs hybrid retrieval (Vector Search + Re-ranking) to find relevant context.
    """
    try:
        result = rag_service.query(request.query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
