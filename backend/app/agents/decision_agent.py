from app.agents.state import AgentState
from app.core.config import settings
from langchain_community.chat_models import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage

class DecisionAgent:
    def __init__(self):
        if settings.USE_BEDROCK:
            self.llm = ChatBedrock(
                model_id=settings.BEDROCK_LLM_MODEL_ID,
                region_name=settings.BEDROCK_REGION,
                model_kwargs={"temperature": 0.1}
            )
        else:
            self.llm = None

    def invoke(self, state: AgentState) -> AgentState:
        print("--- Decision Agent: Making final decision ---")
        summary = state.get("research_summary", "")
        risks = state.get("risk_analysis", "")
        query = state.get("query", "")
        
        if self.llm:
            messages = [
                SystemMessage(content="You are a Decision Agent. Based on the research summary and risk analysis, provide a final recommendation to the user."),
                HumanMessage(content=f"Query: {query}\n\nResearch Summary:\n{summary}\n\nRisk Analysis:\n{risks}")
            ]
            response = self.llm.invoke(messages)
            decision = response.content
        else:
            # Mock Decision Logic
            if "No significant risks" in risks:
                decision = "RECOMMENDATION: Proceed. The data supports the query with low risk."
            else:
                decision = "RECOMMENDATION: Proceed with Caution. Risks were identified that require mitigation."
            
        state["final_decision"] = decision
        state["audit_log"].append(f"Decision Agent outcome: {decision}")
        
        return state
