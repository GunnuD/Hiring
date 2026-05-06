import streamlit as st
import time
from hiring_graph import app, HiringStatus

st.set_page_config(page_title="Automated Hiring Workflow", layout="wide")

st.title("🤖 Automated Hiring Workflow")
st.markdown("Configure and track your hiring process using LangGraph.")

with st.sidebar:
    st.header("Job Configuration")
    job_id = st.text_input("Job ID", value="JOB-2026-001")
    job_title = st.text_input("Job Title", value="Senior Software Engineer")
    
    st.divider()
    st.header("Decision Simulation")
    enough_applicants = st.checkbox("Enough Applicants?", value=True)
    jd_approved = st.checkbox("JD Approved?", value=True)
    candidate_selected = st.checkbox("Candidate Selected?", value=True)
    offer_accepted = st.checkbox("Offer Accepted?", value=True)

if st.button("🚀 Start Hiring Process"):
    st.divider()
    
    # Initial state
    inputs = {
        "job_id": job_id,
        "job_title": job_title,
        "jd_content": "",
        "status": HiringStatus.START,
        "candidates": [],
        "enough_applicants": enough_applicants,
        "jd_approved": jd_approved,
        "candidate_selected": candidate_selected,
        "offer_accepted": offer_accepted
    }

    # Progress and status display
    progress_bar = st.progress(0)
    status_text = st.empty()
    log_container = st.container()
    
    steps = 0
    max_steps = 15 # Approximate
    
    with log_container:
        st.subheader("Workflow Execution Logs")
        for output in app.stream(inputs):
            for node_name, state_update in output.items():
                steps += 1
                progress = min(steps / max_steps, 1.0)
                progress_bar.progress(progress)
                
                # Visual feedback for each step
                with st.expander(f"Step: {node_name.replace('_', ' ').title()}", expanded=True):
                    st.write(f"Node `{node_name}` completed.")
                    if "status" in state_update:
                        st.info(f"New Status: **{state_update['status']}**")
                    if "jd_content" in state_update:
                        st.text_area("Generated JD", state_update["jd_content"], height=100)
                    if "candidates" in state_update:
                        st.success(f"Shortlisted: {state_update['candidates'][0]['name']}")
                
                time.sleep(0.5) # Just for visual effect in the UI

    st.success("✅ Hiring Workflow Sequence Completed!")
    st.balloons()
