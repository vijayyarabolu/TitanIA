from langgraph.graph import StateGraph, END
from app.agents.state import AgentState
from app.agents.research_agent import ResearchAgent
from app.agents.risk_agent import RiskAgent
from app.agents.decision_agent import DecisionAgent
from app.agents.audit_agent import AuditAgent

# Initialize Agents
research_agent = ResearchAgent()
risk_agent = RiskAgent()
decision_agent = DecisionAgent()
audit_agent = AuditAgent()

# Define the Graph
workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("research", research_agent.invoke)
workflow.add_node("risk", risk_agent.invoke)
workflow.add_node("decision", decision_agent.invoke)
workflow.add_node("audit", audit_agent.invoke)

# Define Edges
workflow.set_entry_point("research")
workflow.add_edge("research", "risk")
workflow.add_edge("risk", "decision")
workflow.add_edge("decision", "audit")
workflow.add_edge("audit", END)

# Compile the graph
app_graph = workflow.compile()
