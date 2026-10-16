import streamlit as st
import pandas as pd
import numpy as np
import time
import json
import plotly.express as px
from datetime import datetime
from agents import AGENT_REGISTRY, execute_agent_task
from orchestrator import MasterOrchestrator

st.set_page_config(
    page_title="Agentic AI Office Automation System - Enterprise Edition",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Enterprise Theme
st.markdown("""
<style>
    .main-header { font-size: 2.2rem; font-weight: 700; color: #1E293B; margin-bottom: 0px; }
    .sub-header { font-size: 1rem; color: #64748B; margin-bottom: 20px; }
    .card { background-color: #F8FAFC; padding: 20px; border-radius: 10px; border: 1px solid #E2E8F0; margin-bottom: 15px; }
    .agent-badge { background-color: #0284C7; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.8rem; }
    .status-active { color: #16A34A; font-weight: bold; }
    .status-demo { color: #D97706; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Session State Initialization
if 'mode' not in st.session_state:
    st.session_state.mode = 'Demo Mode'
if 'api_key' not in st.session_state:
    st.session_state.api_key = ''
if 'audit_logs' not in st.session_state:
    st.session_state.audit_logs = []
if 'approval_queue' not in st.session_state:
    st.session_state.approval_queue = [
        {
            'id': 'EML-8021',
            'agent': 'Sales Outreach Specialist',
            'recipient': 'vp_procurement@globalcorp.com',
            'subject': 'Enterprise AI Suite Strategy Discussion',
            'body': 'Dear Team, Based on our recent analysis, we have prepared a tailored enterprise package...',
            'timestamp': '2026-10-16 14:30:00'
        }
    ]

# Sidebar Configuration
with st.sidebar:
    st.title("🤖 System Control")
    st.session_state.mode = st.radio("Operating Mode", ["Demo Mode", "API Mode (OpenAI)"])
    
    if st.session_state.mode == "API Mode (OpenAI)":
        st.session_state.api_key = st.text_input("OpenAI API Key", type="password", value=st.session_state.api_key)
        if not st.session_state.api_key:
            st.warning("⚠️ Enter API key to run live calls.")
        else:
            st.success("API Key Active")
    else:
        st.info("💡 **Demo Mode**: Simulating agent interactions with synthetic responses.")
        
    st.markdown("---")
    st.subheader("System Status")
    st.write(f"**Agents Registered:** {len(AGENT_REGISTRY)}")
    st.write(f"**Orchestrator:** v2.4 Active")
    st.write(f"**Audit Logs:** {len(st.session_state.audit_logs)} entries")

# Header Section
st.markdown('<div class="main-header">Agentic AI Office Automation System</div>', unsafe_allow_html=True)
st.markdown(f'<div class="sub-header">Enterprise Edition | Current Mode: <span class="{"status-demo" if "Demo" in st.session_state.mode else "status-active"}">{st.session_state.mode}</span></div>', unsafe_allow_html=True)

# Main Navigation
tabs = st.tabs(["🏛️ Master Orchestrator", "🤖 Specialized Agents", "📄 Doc Generator", "📊 Data & Excel AI", "📧 Approval Queue", "📜 Audit Logs"])

# Tab 1: Master Orchestrator
with tabs[0]:
    st.subheader("Master-Agent Orchestration Engine")
    st.write("Submit high-level goals. The Master Orchestrator automatically plans, decomposes, and delegates sub-tasks to specialized agents.")
    
    orchestrator_goal = st.text_area("Enter Enterprise Goal / Mission Statement:", 
                                     placeholder="e.g., Conduct a comprehensive Q3 financial review, analyze churn dataset, draft summary report, and email key findings to executive leadership.")
    
    col1, col2 = st.columns([1, 4])
    with col1:
        execute_goal = st.button("🚀 Execute Workflow", use_container_width=True)
        
    if execute_goal and orchestrator_goal:
        st.markdown("### Execution Decomposition")
        orchestrator = MasterOrchestrator(mode=st.session_state.mode, api_key=st.session_state.api_key)
        
        progress_bar = st.progress(0)
        status_box = st.empty()
        
        steps = orchestrator.decompose_goal(orchestrator_goal)
        results = []
        
        for idx, step in enumerate(steps):
            status_box.info(f"Executing Step {idx+1}/{len(steps)}: **[{step['agent']}]** - {step['task']}")
            res = execute_agent_task(step['agent'], step['task'], st.session_state.mode, st.session_state.api_key)
            results.append({"step": idx+1, "agent": step['agent'], "output": res})
            
            # Log action
            st.session_state.audit_logs.append({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "agent": step['agent'],
                "task": step['task'],
                "status": "Success"
            })
            
            progress_bar.progress((idx + 1) / len(steps))
            time.sleep(0.5)
            
        status_box.success("✅ Multi-Agent Workflow Completed Successfully!")
        
        for r in results:
            with st.expander(f"Step {r['step']}: {r['agent']}"):
                st.write(r['output'])

# Tab 2: Specialized Agents Directory
with tabs[1]:
    st.subheader("25 Specialized Enterprise Agents")
    
    departments = list(set([a['dept'] for a in AGENT_REGISTRY.values()]))
    selected_dept = st.selectbox("Filter by Department", ["All Departments"] + departments)
    
    col_a, col_b = st.columns([2, 3])
    
    filtered_agents = {k: v for k, v in AGENT_REGISTRY.items() if selected_dept == "All Departments" or v['dept'] == selected_dept}
    
    with col_a:
        selected_agent_name = st.radio("Select Agent to Test:", list(filtered_agents.keys()))
        
    with col_b:
        agent_info = AGENT_REGISTRY[selected_agent_name]
        st.markdown(f"### {selected_agent_name}")
        st.markdown(f"**Department:** {agent_info['dept']}")
        st.markdown(f"**Role & Expertise:** {agent_info['role']}")
        
        agent_input = st.text_area("Provide specific input/prompt for agent:", height=100)
        if st.button("Run Agent"):
            if agent_input:
                with st.spinner("Agent working..."):
                    res = execute_agent_task(selected_agent_name, agent_input, st.session_state.mode, st.session_state.api_key)
                    st.markdown("#### Agent Output:")
                    st.info(res)
                    st.session_state.audit_logs.append({
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "agent": selected_agent_name,
                        "task": agent_input,
                        "status": "Success"
                    })
            else:
                st.warning("Please provide input text.")

# Tab 3: Document Generator
with tabs[2]:
    st.subheader("Autonomous Document Generator")
    doc_type = st.selectbox("Select Document Type", ["Executive Brief", "Quarterly Financial Analysis", "Technical Architecture Proposal", "HR Policy Brief"])
    doc_title = st.text_input("Document Title", "Q3 2026 Enterprise Performance Review")
    doc_prompt = st.text_area("Key Topics & Requirements", "Include revenue metrics, operational efficiency highlights, risks, and strategic roadmap for Q4.")
    
    if st.button("Generate Document"):
        with st.spinner("Drafting document with specialized agents..."):
            res = execute_agent_task("Corporate Communications Officer", f"Generate a detailed {doc_type} titled '{doc_title}' based on: {doc_prompt}", st.session_state.mode, st.session_state.api_key)
            st.markdown("---")
            st.markdown(f"# {doc_title}")
            st.markdown(res)
            st.download_button("📥 Download Markdown (.md)", res, file_name=f"{doc_title.lower().replace(' ', '_')}.md")

# Tab 4: Excel & Data AI Analyzer
with tabs[3]:
    st.subheader("Interactive Excel & Data AI Analyzer")
    uploaded_file = st.file_uploader("Upload CSV or Excel dataset", type=["csv", "xlsx"])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
        st.write("### Dataset Preview")
        st.dataframe(df.head())
        
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            st.write("### Data Summary")
            st.write(df.describe())
        with col_d2:
            st.write("### Quick Chart")
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            if len(numeric_cols) >= 2:
                x_axis = st.selectbox("X Axis", df.columns)
                y_axis = st.selectbox("Y Axis", numeric_cols)
                fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} by {x_axis}")
                st.plotly_chart(fig, use_container_width=True)
                
        if st.button("🤖 Run Automated AI Data Audit"):
            data_summary = f"Columns: {list(df.columns)}, Shape: {df.shape}, Summary: {df.describe().to_string()}"
            res = execute_agent_task("Data Analytics Lead", f"Analyze this dataset summary and report anomalies, key trends, and statistical insights: {data_summary}", st.session_state.mode, st.session_state.api_key)
            st.markdown("### AI Analysis Results")
            st.info(res)

# Tab 5: Approval Queue
with tabs[4]:
    st.subheader("Human-in-the-Loop Email & Action Approval Queue")
    st.write("Review, edit, and approve agent-generated external communications before transmission.")
    
    if not st.session_state.approval_queue:
        st.success("No pending items requiring human approval.")
    else:
        for idx, item in enumerate(st.session_state.approval_queue):
            with st.expander(f"📌 [{item['id']}] {item['subject']} (Agent: {item['agent']})", expanded=True):
                col_e1, col_e2 = st.columns([3, 1])
                with col_e1:
                    rec = st.text_input(f"Recipient ({item['id']})", value=item['recipient'])
                    subj = st.text_input(f"Subject ({item['id']})", value=item['subject'])
                    body = st.text_area(f"Body ({item['id']})", value=item['body'], height=150)
                with col_e2:
                    st.write("**Actions**")
                    if st.button(f"✅ Approve & Send", key=f"app_{idx}"):
                        st.session_state.approval_queue.pop(idx)
                        st.session_state.audit_logs.append({
                            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "agent": item['agent'],
                            "task": f"Email sent to {rec}: {subj}",
                            "status": "APPROVED & SENT"
                        })
                        st.success(f"Email {item['id']} sent successfully!")
                        st.rerun()
                    if st.button(f"❌ Reject", key=f"rej_{idx}"):
                        st.session_state.approval_queue.pop(idx)
                        st.warning(f"Item {item['id']} rejected.")
                        st.rerun()

# Tab 6: Audit Logs
with tabs[5]:
    st.subheader("Persistent Audit Trail & System Logs")
    if st.session_state.audit_logs:
        audit_df = pd.DataFrame(st.session_state.audit_logs)
        st.dataframe(audit_df, use_container_width=True)
    else:
        st.info("No logs recorded in current session.")
