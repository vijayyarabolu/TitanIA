from app.agents.state import AgentState
from app.services.rag_service import RAGService
from app.core.config import settings
from langchain_community.chat_models import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage

class ResearchAgent:
    def __init__(self):
        self.rag_service = RAGService()
        if settings.USE_BEDROCK:
            self.llm = ChatBedrock(
                model_id=settings.BEDROCK_LLM_MODEL_ID,
                region_name=settings.BEDROCK_REGION,
                model_kwargs={"temperature": 0.1}
            )
        else:
            self.llm = None

    def invoke(self, state: AgentState) -> AgentState:
        query = state["query"]
        print(f"--- Research Agent: Searching for '{query}' ---")
        
        # Use RAG Service to get context
        rag_result = self.rag_service.query(query)
        
        context = rag_result["context"]
        documents = rag_result["source_documents"]
        
        if self.llm:
            messages = [
                SystemMessage(content="You are a Research Agent. Summarize the following context to answer the user's query."),
                HumanMessage(content=f"Query: {query}\n\nContext:\n{context}")
            ]
            response = self.llm.invoke(messages)
            summary = response.content
        else:
            # Fallback to raw context
            summary = f"Based on the documents found:\n{context}"
        
        state["documents"] = documents
        state["research_summary"] = summary
        state["audit_log"].append(f"Research Agent found {len(documents)} documents.")
        
        return state
