from app.agents.state import AgentState
import json
import os

class AuditAgent:
    def invoke(self, state: AgentState) -> AgentState:
        print("--- Audit Agent: Logging execution ---")
        
        log_entry = {
            "query": state["query"],
            "decision": state["final_decision"],
            "audit_trail": state["audit_log"]
        }
        
        # Save to a local log file
        with open("audit_log.jsonl", "a") as f:
            f.write(json.dumps(log_entry) + "\n")
            
        return state
