import json
from agents_g6 import AGENT_REGISTRY

class MasterOrchestrator:
    def __init__(self, mode="Demo Mode", api_key=""):
        self.mode = mode
        self.api_key = api_key

    def decompose_goal(self, goal: str):
        plan = [
            {"agent": "Executive Leadership Director #1", "task": f"Analyze high-level directive and establish strategic framework for: {goal}"},
            {"agent": "Finance & Accounting Senior Lead #1", "task": "Evaluate budgetary impact and financial feasibility."},
            {"agent": "Legal & Compliance Specialist #1", "task": "Perform regulatory risk assessment and compliance verification."},
            {"agent": "Operations & Logistics Director #2", "task": "Coordinate multi-departmental execution roadmap."},
            {"agent": "Data & Analytics Analyst #5", "Task": "Synthesize final operational metrics and generate executive summary."}
        ]
        return plan
