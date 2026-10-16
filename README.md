# Agentic AI Office Automation System - Enterprise Edition

An enterprise-grade multi-agent AI office automation system built with **Streamlit** and **OpenAI GPT-4o**.

## Features

- **Master-Agent Orchestrator**: Automatically decomposes complex enterprise goals into multi-step agent execution plans.
- **25 Specialized Agents**: Categorized into Executive, Finance, HR & Operations, Sales & Marketing, and IT & Engineering.
- **Dual Operating Mode**:
  - **Demo Mode**: Zero-cost offline testing with deterministic responses.
  - **API Mode**: Live integration with OpenAI API (`gpt-4o-mini` / `gpt-4o`).
- **Autonomous Document Generator**: Generates executive briefs, reports, and proposals with Markdown export.
- **Data & Excel AI Analyzer**: Interactive data analysis, Plotly chart generation, and automated anomaly auditing.
- **Human-in-the-Loop Approval Queue**: Review, edit, approve, or reject email drafts and sensitive actions.
- **Persistent Audit Log**: Full visibility into agent activities and execution history.

## Setup & Running Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-org/agentic-ai-office-automation.git
   cd agentic-ai-office-automation
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

4. **Configuration**:
   - By default, the application runs in **Demo Mode**.
   - To use live AI generation, toggle to **API Mode (OpenAI)** in the sidebar and enter your OpenAI API key.

## Docker Deployment

```bash
docker build -t agentic-office-ai .
docker run -p 8501:8501 agentic-office-ai
```
