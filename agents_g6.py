import os
from openai import OpenAI

DEPARTMENTS = [
    "Executive Leadership", "Finance & Accounting", "Legal & Compliance", 
    "Operations & Logistics", "Human Resources", "Sales & Business Dev", 
    "Marketing & Growth", "IT & Cybersecurity", "Data & Analytics", "Research & Development"
]

AGENT_REGISTRY = {}
roles_templates = [
    ("Director", "Strategic oversight, resource allocation, and executive decision-making."),
    ("Senior Lead", "Process optimization, quality control, and advanced execution."),
    ("Specialist", "Operational execution, anomaly detection, and reporting."),
    ("Analyst", "Data synthesis, metric tracking, and forecasting."),
    ("Consultant", "Advisory, regulatory compliance, and risk mitigation.")
]

agent_id_counter = 1
for dept in DEPARTMENTS:
    for i in range(50):
        title_type, role_desc = roles_templates[i % len(roles_templates)]
        agent_name = f"{dept} {title_type} #{i+1}"
        AGENT_REGISTRY[agent_name] = {
            "id": f"{agent_id_counter:03d}",
            "dept": dept,
            "role": f"{role_desc} Specialized in {dept.lower()} workflows and automated enterprise execution."
        }
        agent_id_counter += 1

DEMO_RESPONSES = {
    "Executive Leadership Director #1": "[500-AGENT MESH - GPT-6 LUNA (TEMP 1.0) DEMO MODE] Executive Strategy Approved: Global operational expansion and AI integration initiated across all 10 departments.",
}

def execute_agent_task(agent_name: str, task_prompt: str, mode: str = "Demo Mode", api_key: str = None, model_choice: str = "gpt-6-luna", reasoning_effort: str = "medium") -> str:
    if mode == "Demo Mode" or not api_key:
        return DEMO_RESPONSES.get(agent_name, f"[GPT-6 Luna | Temp 1.0] Task processed by {agent_name} using [{model_choice}]. Instructions: '{task_prompt[:60]}...'.")
    
    try:
        client = OpenAI(api_key=api_key)
        agent_info = AGENT_REGISTRY.get(agent_name, {"dept": "Enterprise", "role": "Autonomous Agent"})
        
        response = client.chat.completions.create(
            model=model_choice,
            messages=[
                {"role": "system", "content": f"You are {agent_name}, an expert enterprise AI agent in {agent_info['dept']}. Role: {agent_info['role']}. Provide professional, highly detailed, and actionable enterprise outputs."},
                {"role": "user", "content": task_prompt}
            ],
            reasoning_effort=reasoning_effort if model_choice.startswith("gpt-6") else None,
            temperature=1.0  # Temperature explicitly set to 1.0 as requested
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error executing task via OpenAI API ({model_choice}): {str(e)}"
