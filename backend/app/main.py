from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import ingestion_routes, rag_routes, agent_routes

app = FastAPI(title="TitanIA Enterprise AI Platform", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingestion_routes.router, prefix="/api/v1/ingestion", tags=["Ingestion"])
app.include_router(rag_routes.router, prefix="/api/v1/rag", tags=["RAG"])
app.include_router(agent_routes.router, prefix="/api/v1/agents", tags=["Agents"])

@app.get("/")
def read_root():
    return {"message": "Welcome to TitanIA API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
