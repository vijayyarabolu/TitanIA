from typing import TypedDict, List, Dict, Any

class AgentState(TypedDict):
    query: str
    messages: List[Dict[str, str]]  # Chat history
    documents: List[Dict[str, Any]] # Retrieved documents
    research_summary: str           # Output from Research Agent
    risk_analysis: str              # Output from Risk Agent
    final_decision: str             # Output from Decision Agent
    audit_log: List[str]            # Log of steps taken
