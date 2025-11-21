from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agents.graph import app_graph

router = APIRouter()

class AgentRequest(BaseModel):
    query: str

@router.post("/run", summary="Run the Multi-Agent Workflow")
async def run_agent_workflow(request: AgentRequest):
    """
    Triggers the LangGraph workflow: Research -> Risk -> Decision -> Audit.
    """
    try:
        initial_state = {
            "query": request.query,
            "messages": [],
            "documents": [],
            "research_summary": "",
            "risk_analysis": "",
            "final_decision": "",
            "audit_log": []
        }
        
        # Invoke the graph
        final_state = await app_graph.ainvoke(initial_state)
        
        return {
            "query": final_state["query"],
            "decision": final_state["final_decision"],
            "risk_analysis": final_state["risk_analysis"],
            "audit_log": final_state["audit_log"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
