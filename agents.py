import os
from openai import OpenAI

# 25 Specialized Enterprise Agents Organized by Department
AGENT_REGISTRY = {
    # Executive & Strategy
    "Chief Executive Agent": {"dept": "Executive", "role": "High-level goal decomposition and strategic governance."},
    "Corporate Strategy Planner": {"dept": "Executive", "role": "Market analysis, competitive intelligence, and growth roadmaps."},
    "Legal & Compliance Officer": {"dept": "Executive", "role": "Regulatory compliance, contract risk audit, and policy checks."},
    "Corporate Communications Officer": {"dept": "Executive", "role": "Executive drafting, press releases, and internal announcements."},
    "Risk & Governance Analyst": {"dept": "Executive", "role": "Operational risk matrix calculation and mitigation planning."},

    # Finance & Accounting
    "Chief Financial Agent": {"dept": "Finance", "role": "Capital allocation, financial health checks, and budget planning."},
    "Financial Analyst": {"dept": "Finance", "role": "P&L variance analysis, forecasting, and expense auditing."},
    "Payroll & Invoicing Specialist": {"dept": "Finance", "role": "Automated ledger checking, billing reconciliation, and invoice drafts."},
    "Tax & Audit Compliance Agent": {"dept": "Finance", "role": "Tax policy alignment, deduction verification, and audit trail validation."},
    "Procurement & Cost Optimizer": {"dept": "Finance", "role": "Vendor cost benchmarking and procurement negotiation strategies."},

    # Operations & HR
    "Operations Manager": {"dept": "Operations", "role": "Process bottleneck identification and workflow optimization."},
    "Talent Acquisition Recruiter": {"dept": "HR", "role": "Candidate resume screening, job description drafting, and interviewing guidelines."},
    "HR Policy Specialist": {"dept": "HR", "role": "Employee handbook inquiries, onboarding workflows, and benefit summaries."},
    "Facilities & Logistics Agent": {"dept": "Operations", "role": "Office inventory tracking, supply chain logistics, and space planning."},
    "Customer Support Director": {"dept": "Operations", "role": "Escalated ticket resolution and customer satisfaction analysis."},

    # Sales & Marketing
    "Sales Strategy Lead": {"dept": "Sales", "role": "Pipeline forecasting, territory planning, and deal closing support."},
    "Sales Outreach Specialist": {"dept": "Sales", "role": "Cold email generation, lead qualifying, and follow-up sequences."},
    "Marketing Content Creator": {"dept": "Marketing", "role": "Blog posts, ad copy, landing page text, and social campaigns."},
    "SEO & Digital Strategist": {"dept": "Marketing", "role": "Keyword strategy, content optimization, and search rank tactics."},
    "Market Research Analyst": {"dept": "Marketing", "role": "Customer sentiment analysis and competitor benchmarking."},

    # IT & Engineering
    "Chief Technology Agent": {"dept": "IT", "role": "IT architecture decisions, tech stack evaluation, and AI adoption."},
    "Cybersecurity Auditor": {"dept": "IT", "role": "Vulnerability assessment, security log audit, and policy enforcement."},
    "DevOps & Infrastructure Lead": {"dept": "IT", "role": "CI/CD deployment monitoring, server health, and cloud cost control."},
    "Data Analytics Lead": {"dept": "IT", "role": "Statistical data analysis, dataset anomaly detection, and insights summary."},
    "Software QA Specialist": {"dept": "IT", "role": "Test suite drafting, bug report analysis, and code quality review."}
}

DEMO_RESPONSES = {
    "Chief Executive Agent": "[DEMO RESPONSE] Strategic Objectives Identified: 1. Expand Enterprise Market Share by 15%. 2. Streamline cross-departmental AI automation workflows.",
    "Corporate Strategy Planner": "[DEMO RESPONSE] Market analysis completed: Strong growth opportunities in AI-assisted document workflows.",
    "Legal & Compliance Officer": "[DEMO RESPONSE] Regulatory Risk Level: LOW. Terms align with standard enterprise compliance standards.",
    "Corporate Communications Officer": "[DEMO RESPONSE] Executive Memo Drafted: 'Q3 Enterprise Performance Summary and AI Transformation Roadmap'.",
    "Chief Financial Agent": "[DEMO RESPONSE] Q3 Financial Summary: Net Margin +12.4% YoY. OpEx reduced by 8% via automation.",
    "Financial Analyst": "[DEMO RESPONSE] Financial Forecast: Projected revenue for Q4 estimated at $4.2M based on linear growth trends.",
    "Data Analytics Lead": "[DEMO RESPONSE] Data Audit Findings: Sample dataset contains 0 null values. Outlier detected in column 'Revenue' row #42.",
    "Sales Outreach Specialist": "[DEMO RESPONSE] Email Draft: Subject: 'Scaling AI Operations at Your Enterprise'. Status: Queued for Human Approval."
}

def execute_agent_task(agent_name: str, task_prompt: str, mode: str = "Demo Mode", api_key: str = None) -> str:
    if mode == "Demo Mode" or not api_key:
        return DEMO_RESPONSES.get(agent_name, f"[DEMO RESPONSE] Task executed successfully by {agent_name} for prompt: '{task_prompt[:50]}...'. All parameters verified.")
    
    try:
        client = OpenAI(api_key=api_key)
        agent_info = AGENT_REGISTRY.get(agent_name, {"role": "Enterprise Assistant"})
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"You are {agent_name}, an expert enterprise AI agent in {agent_info.get('dept', 'General')}. Role: {agent_info['role']}. Provide professional, concise, and actionable outputs."},
                {"role": "user", "content": task_prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error executing agent task via OpenAI API: {str(e)}"
