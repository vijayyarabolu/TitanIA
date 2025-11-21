from app.agents.state import AgentState
from app.core.config import settings
try:
    from langchain_aws import ChatBedrock
except ImportError:
    from langchain_community.chat_models.bedrock import BedrockChat as ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage

class RiskAgent:
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
        print("--- Risk Agent: Analyzing risks ---")
        summary = state.get("research_summary", "")
        
        if self.llm:
            messages = [
                SystemMessage(content="You are a Risk Agent. Analyze the following summary for any potential risks, compliance issues, or uncertainties."),
                HumanMessage(content=f"Summary:\n{summary}")
            ]
            response = self.llm.invoke(messages)
            risk_analysis = response.content
        else:
            # Mock Risk Analysis Logic
            risks = []
            if "confidential" in summary.lower():
                risks.append("Potential data privacy issue detected.")
            if "uncertain" in summary.lower():
                risks.append("High uncertainty in source data.")
                
            if not risks:
                risk_analysis = "No significant risks detected."
            else:
                risk_analysis = "Risks Identified:\n- " + "\n- ".join(risks)
            
        state["risk_analysis"] = risk_analysis
        state["audit_log"].append(f"Risk Agent analysis: {risk_analysis}")
        
        return state
