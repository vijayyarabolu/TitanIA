from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.ingestion_service import IngestionService

router = APIRouter()
ingestion_service = IngestionService()

@router.post("/upload", summary="Upload and ingest a document")
async def upload_document(file: UploadFile = File(...)):
    """
    Uploads a document (PDF, TXT, CSV), saves it to S3 (mock),
    chunks it, and indexes it in the Vector DB.
    """
    try:
        result = await ingestion_service.process_document(file)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
