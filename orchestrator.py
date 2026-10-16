import json
from agents import AGENT_REGISTRY

class MasterOrchestrator:
    def __init__(self, mode="Demo Mode", api_key=""):
        self.mode = mode
        self.api_key = api_key

    def decompose_goal(self, goal: str):
        """
        Decomposes a complex goal into step-by-step sub-tasks and assigns them to relevant agents.
        """
        # Simple intelligent heuristics for demo/decomposition
        goal_lower = goal.lower()
        plan = []

        if "financial" in goal_lower or "revenue" in goal_lower or "q3" in goal_lower:
            plan.append({"agent": "Chief Financial Agent", "task": f"Extract financial KPIs and metrics relevant to: {goal}"})
            plan.append({"agent": "Financial Analyst", "task": "Perform P&L analysis and variance checks."})
            plan.append({"agent": "Corporate Communications Officer", "task": "Draft executive summary report from financial findings."})
        elif "marketing" in goal_lower or "sales" in goal_lower or "outreach" in goal_lower:
            plan.append({"agent": "Sales Strategy Lead", "task": f"Define target segments for: {goal}"})
            plan.append({"agent": "Sales Outreach Specialist", "task": "Draft personalized outreach sequence."})
            plan.append({"agent": "Legal & Compliance Officer", "task": "Review outreach templates for compliance."})
        else:
            plan.append({"agent": "Chief Executive Agent", "task": f"Define strategic framework for: {goal}"})
            plan.append({"agent": "Operations Manager", "task": "Identify execution requirements and bottlenecks."})
            plan.append({"agent": "Corporate Communications Officer", "task": "Produce final operational summary."})

        return plan
