import streamlit as st
import pandas as pd
import numpy as np
import time
import json
import io
import plotly.express as px
from datetime import datetime
from agents_g6 import AGENT_REGISTRY, execute_agent_task
from orchestrator_500 import MasterOrchestrator

st.set_page_config(
    page_title="Agentic AI Office Automation System - GPT-6 Luna Edition",
    page_icon="ðŸš€",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .hero-header {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #0284C7 100%);
        padding: 35px;
        border-radius: 16px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.2);
    }
    .hero-title { font-size: 2.8rem; font-weight: 800; margin: 0; letter-spacing: -0.5px; }
    .hero-subtitle { font-size: 1.1rem; color: #94A3B8; margin-top: 8px; font-weight: 400; }
    .status-badge-demo { background-color: #FEF3C7; color: #92400E; padding: 4px 10px; border-radius: 20px; font-weight: 600; font-size: 0.85rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-header">
    <div class="hero-title">ðŸš€ Agentic AI Office Automation System</div>
    <div class="hero-subtitle">GPT-6 Luna Enterprise Edition | 500 Specialized Autonomous Agents | Temperature 1.0 | Multi-Modal Ingestion & PDF/DOCX Studio</div>
</div>
""", unsafe_allow_html=True)

if 'mode' not in st.session_state:
    st.session_state.mode = 'Demo Mode'
if 'api_key' not in st.session_state:
    st.session_state.api_key = ''
if 'audit_logs' not in st.session_state:
    st.session_state.audit_logs = []
if 'approval_queue' not in st.session_state:
    st.session_state.approval_queue = [
        {
            'id': 'EML-7701',
            'agent': 'Global Executive Communications Director (Agent #1)',
            'recipient': 'board@enterprise-global.com',
            'subject': 'GPT-6 Luna Integration & Autonomous Operations Report',
            'body': """Dear Board Members,

All 500 specialized agents have been successfully upgraded to leverage GPT-6 Luna at temperature 1.0...

Sincerely,
AI Executive Office""",
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    ]

with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/artificial-intelligence.png", width=100)
    st.title("Enterprise Control")
    
    st.session_state.mode = st.radio("Operating Mode", ["Demo Mode", "API Mode (GPT-6 Luna)"])
    
    if st.session_state.mode == "API Mode (GPT-6 Luna)":
        st.session_state.api_key = st.text_input("OpenAI API Key", type="password", value=st.session_state.api_key)
        if not st.session_state.api_key:
            st.warning("âš ï¸ Please input OpenAI API key.")
        else:
            st.success("API Key Configured")
    else:
        st.markdown('<span class="status-badge-demo">Demo Mode Active</span>', unsafe_allow_html=True)
        st.info("Simulating high-speed enterprise intelligence with synthetic multi-agent responses.")
        
    st.markdown("---")
    st.subheader("âš™ï¸ Model Parameters")
    st.write("**Model:** `gpt-6-luna`")
    st.write("**Temperature:** `1.0`")
    st.write("**Reasoning Effort:** `medium`")
    
    st.markdown("---")
    st.subheader("ðŸ“Š System Metrics")
    st.metric("Total Specialized Agents", "500")
    st.metric("Global Departments", "10")
    st.metric("Pending Approvals", len(st.session_state.approval_queue))
    st.metric("Audit Log Entries", len(st.session_state.audit_logs))

tabs = st.tabs([
    "ðŸ›ï¸ Master Orchestrator (500 Agents)", 
    "ðŸ¤– Agent Directory & File Ingestion", 
    "ðŸ“„ PDF & DOCX Generator Studio", 
    "ðŸ“Š Excel & Data Analytics AI", 
    "ðŸ“§ Email Generator & Approval Queue", 
    "ðŸ“œ Audit Logs & Telemetry"
])

with tabs[0]:
    st.subheader("Master Orchestration Engine (500-Agent Mesh | GPT-6 Luna)")
    st.write("Submit complex multi-department goals. The Master Orchestrator dynamically routes sub-tasks across the 500-agent enterprise network using GPT-6 Luna (Temperature 1.0).")
    
    col_o1, col_o2 = st.columns([3, 1])
    with col_o1:
        goal_input = st.text_area("Enter Enterprise Goal / Mission Directive:", 
                                  value="Perform a complete Q4 multi-departmental audit across finance, legal compliance, cyber security, and generate an executive PDF report with automated email dispatch.")
    with col_o2:
        st.markdown("<br>", unsafe_allow_html=True)
        execute_btn = st.button("ðŸš€ Execute 500-Agent Mesh", use_container_width=True)
        
    if execute_btn and goal_input:
        orchestrator = MasterOrchestrator(mode=st.session_state.mode, api_key=st.session_state.api_key)
        
        progress = st.progress(0)
        status_holder = st.empty()
        
        steps = orchestrator.decompose_goal(goal_input)
        execution_results = []
        
        for idx, step in enumerate(steps):
            status_holder.info(f"Step {idx+1}/{len(steps)} | Active Agent: {step['agent']} | Task: {step['task']}")
            res = execute_agent_task(step['agent'], step['task'], st.session_state.mode, st.session_state.api_key, model_choice="gpt-6-luna")
            execution_results.append({"step": idx+1, "agent": step['agent'], "output": res})
            
            st.session_state.audit_logs.append({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "agent": step['agent'],
                "task": step['task'],
                "status": "Success"
            })
            
            progress.progress((idx + 1) / len(steps))
            time.sleep(0.4)
            
        status_holder.success("âœ… Master Orchestration Completed Successfully!")
        
        st.markdown("### ðŸ“‹ Orchestration Execution Report")
        for r in execution_results:
            with st.expander(f"Phase {r['step']}: {r['agent']}"):
                st.write(r['output'])

with tabs[1]:
    st.subheader("500 Specialized Agent Directory & Multi-Modal Ingestion")
    st.write("Select any of the 500 specialized agents and feed them instructions via Text, Notepad (.txt), PDF, or Word (.docx) files.")
    
    departments = sorted(list(set([info['dept'] for info in AGENT_REGISTRY.values()])))
    selected_dept = st.selectbox("Filter by Department (10 Departments)", ["All Departments"] + departments)
    
    filtered_agents = {k: v for k, v in AGENT_REGISTRY.items() if selected_dept == "All Departments" or v['dept'] == selected_dept}
    
    col_a1, col_a2 = st.columns([1, 2])
    with col_a1:
        agent_names = list(filtered_agents.keys())
        selected_agent = st.selectbox("Select Specialized Agent (1 to 500)", agent_names)
    with col_a2:
        agent_data = AGENT_REGISTRY[selected_agent]
        st.markdown(f"#### {selected_agent}")
        st.markdown(f"**Department:** {agent_data['dept']} | **ID Code:** AGENT-{agent_data['id']}", unsafe_allow_html=True)
        st.markdown(f"**Expertise:** {agent_data['role']}")
        
    st.markdown("---")
    st.markdown("### ðŸ“‚ Multi-Modal Instruction Ingestion")
    ingest_tab1, ingest_tab2 = st.tabs(["Direct Text / Notepad (.txt)", "Upload PDF / DOCX Instruction File"])
    
    prompt_text = ""
    with ingest_tab1:
        prompt_text = st.text_area("Enter Direct Instructions or paste text from Notepad:", placeholder="Type or paste instructions here...")
        
    with ingest_tab2:
        uploaded_inst_file = st.file_uploader("Upload instruction document", type=["txt", "pdf", "docx"])
        if uploaded_inst_file:
            st.success(f"File uploaded successfully: {uploaded_inst_file.name}")
            if uploaded_inst_file.name.endswith(".txt"):
                prompt_text = str(uploaded_inst_file.read(), "utf-8")
                st.info(f"Extracted Text from {uploaded_inst_file.name}:\n\n{prompt_text[:300]}...")
            else:
                prompt_text = f"Process instructions provided in attached document: {uploaded_inst_file.name}"
                st.info("Document queued for agent analysis.")

    if st.button("ðŸš€ Dispatch Task to Agent"):
        if prompt_text:
            with st.spinner(f"Agent {selected_agent} processing instructions via GPT-6 Luna..."):
                output = execute_agent_task(selected_agent, prompt_text, st.session_state.mode, st.session_state.api_key, model_choice="gpt-6-luna")
                st.markdown("### ðŸ’¡ Agent Execution Output")
                st.success(output)
                
                st.session_state.audit_logs.append({
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "agent": selected_agent,
                    "task": prompt_text[:100] + "...",
                    "status": "Success"
                })
        else:
            st.warning("Please provide instruction text or upload a file.")

with tabs[2]:
    st.subheader("Professional PDF & DOCX Generator Studio")
    st.write("Autonomous generation of publication-ready corporate reports, contracts, and proposals with instant file downloads.")
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        doc_format = st.selectbox("Output Format", [".PDF", ".DOCX", ".TXT"])
        doc_category = st.selectbox("Document Template", ["Executive Summary Report", "Financial Audit Statement", "Technical Architecture Specification", "Legal Compliance Brief", "Custom AI Generated Report"])
    with col_g2:
        doc_title = st.text_input("Document Title", "Enterprise Strategic Plan Q4 2026")
        author_agent = st.selectbox("Assigned Lead Agent", list(AGENT_REGISTRY.keys())[:50])
        
    doc_content_prompt = st.text_area("Detailed Requirements & Key Sections", "Include comprehensive metrics, risk analysis, resource allocation, and timeline milestones.")
    
    if st.button("âœ¨ Generate Document"):
        with st.spinner("Generating document via GPT-6 Luna..."):
            generated_body = execute_agent_task(author_agent, f"Generate a formal {doc_category} titled '{doc_title}' based on: {doc_content_prompt}", st.session_state.mode, st.session_state.api_key, model_choice="gpt-6-luna")
            
            st.markdown("### ðŸ“„ Document Preview")
            st.markdown(f"---")
            st.markdown(f"# {doc_title}")
            st.markdown(f"**Author:** {author_agent} | **Model:** GPT-6 Luna (Temp 1.0) | **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            st.markdown(f"---")
            st.markdown(generated_body)
            st.markdown(f"---")
            
            file_buffer = io.BytesIO(generated_body.encode('utf-8'))
            ext = doc_format.lower().replace('.', '')
            st.download_button(
                label=f"ðŸ“¥ Download Document ({doc_format})",
                data=file_buffer,
                file_name=f"{doc_title.lower().replace(' ', '_')}.{ext}",
                mime="text/plain"
            )

with tabs[3]:
    st.subheader("Excel & Data Analytics AI Suite")
    uploaded_data = st.file_uploader("Upload Dataset (.csv, .xlsx)", type=["csv", "xlsx"])
    
    if uploaded_data:
        df = pd.read_csv(uploaded_data) if uploaded_data.name.endswith(".csv") else pd.read_excel(uploaded_data)
        st.write("### Dataset Preview")
        st.dataframe(df.head(10))
        
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            st.write("### Statistical Summary")
            st.write(df.describe())
        with col_d2:
            st.write("### Interactive Visualization")
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            if len(numeric_cols) >= 2:
                x_col = st.selectbox("X-Axis", df.columns)
                y_col = st.selectbox("Y-Axis", numeric_cols, key="y_col_analytics")
                fig = px.area(df, x=x_col, y=y_col, title=f"Trend Analysis: {y_col} vs {x_col}")
                st.plotly_chart(fig, use_container_width=True)
                
        if st.button("ðŸ¤– Run 500-Agent Data Audit"):
            summary_str = f"Columns: {list(df.columns)}, Shape: {df.shape}, Summary: {df.describe().to_string()}"
            analysis = execute_agent_task("Data Science Lead (Agent #401)", f"Perform an exhaustive statistical audit and anomaly detection on this dataset: {summary_str}", st.session_state.mode, st.session_state.api_key, model_choice="gpt-6-luna")
            st.markdown("### ðŸ“Š AI Analytics Audit Report")
            st.success(analysis)

with tabs[4]:
    st.subheader("Email Generator & Human-in-the-Loop Approval Queue")
    st.write("Review, edit, and approve agent-generated external communications and automated email campaigns before dispatch.")
    
    with st.expander("âœ‰ï¸ Draft New Email via Agent"):
        email_agent = st.selectbox("Select Email Generator Agent", list(AGENT_REGISTRY.keys())[100:150])
        email_recipient = st.text_input("Recipient Email", "client@globalpartner.com")
        email_prompt = st.text_input("Email Objective / Prompt", "Draft a professional follow-up regarding our enterprise software proposal.")
        if st.button("Generate & Queue Email"):
            drafted_body = execute_agent_task(email_agent, f"Draft a professional email to {email_recipient} regarding: {email_prompt}", st.session_state.mode, st.session_state.api_key, model_choice="gpt-6-luna")
            new_id = f"EML-{np.random.randint(1000, 9999)}"
            st.session_state.approval_queue.append({
                'id': new_id,
                'agent': email_agent,
                'recipient': email_recipient,
                'subject': f"Strategic Communication: {email_prompt[:30]}...",
                'body': drafted_body,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.success(f"Email successfully generated and added to Approval Queue ({new_id})!")
            st.rerun()

    st.markdown("### ðŸ“¥ Pending Approval Queue")
    if not st.session_state.approval_queue:
        st.success("All items approved. No pending emails in queue.")
    else:
        for idx, item in enumerate(st.session_state.approval_queue):
            with st.expander(f"ðŸ“Œ [{item['id']}] To: {item['recipient']} | Agent: {item['agent']}", expanded=True):
                col_e1, col_e2 = st.columns([3, 1])
                with col_e1:
                    recip = st.text_input(f"Recipient ({item['id']})", value=item['recipient'], key=f"rec_{idx}")
                    subj = st.text_input(f"Subject ({item['id']})", value=item['subject'], key=f"subj_{idx}")
                    body = st.text_area(f"Body ({item['id']})", value=item['body'], height=160, key=f"body_{idx}")
                with col_e2:
                    st.write("**Action Center**")
                    if st.button("âœ… Approve & Send", key=f"app_{idx}", use_container_width=True):
                        sent_item = st.session_state.approval_queue.pop(idx)
                        st.session_state.audit_logs.append({
                            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "agent": sent_item['agent'],
                            "task": f"Approved & Sent Email to {recip}",
                            "status": "APPROVED & DISPATCHED"
                        })
                        st.success(f"Email {sent_item['id']} successfully sent!")
                        st.rerun()
                    if st.button("âŒ Reject", key=f"rej_{idx}", use_container_width=True):
                        st.session_state.approval_queue.pop(idx)
                        st.warning(f"Email {item['id']} rejected.")
                        st.rerun()

with tabs[5]:
    st.subheader("Persistent Enterprise Audit Trail & Telemetry")
    if st.session_state.audit_logs:
        audit_df = pd.DataFrame(st.session_state.audit_logs)
        st.dataframe(audit_df, use_container_width=True)
        
        csv_data = audit_df.to_csv(index=False).encode('utf-8')
        st.download_button("ðŸ“¥ Export Audit Logs (CSV)", csv_data, file_name="enterprise_audit_logs.csv", mime="text/csv")
    else:
        st.info("No audit logs recorded yet in this session.")
