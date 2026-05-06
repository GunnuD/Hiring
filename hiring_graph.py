from typing import Annotated, TypedDict, List
from enum import Enum
from langgraph.graph import StateGraph, END

class HiringStatus(str, Enum):
    START = "START"
    HIRING_REQUEST = "HIRING_REQUEST"
    CREATE_JD = "CREATE_JD"
    REVIEW_JD = "REVIEW_JD"
    POST_JD = "POST_JD"
    MONITOR_APPLICATIONS = "MONITOR_APPLICATIONS"
    SHORTLIST = "SHORTLIST"
    MODIFY_JD = "MODIFY_JD"
    WAIT_48_HOURS = "WAIT_48_HOURS"
    SCHEDULE_INTERVIEW = "SCHEDULE_INTERVIEW"
    CONDUCT_INTERVIEW = "CONDUCT_INTERVIEW"
    INTERVIEW_FEEDBACK = "INTERVIEW_FEEDBACK"
    REJECT_EMAIL = "REJECT_EMAIL"
    SEND_OFFER_LETTER = "SEND_OFFER_LETTER"
    RENEGOTIATE = "RENEGOTIATE"
    ONBOARDING = "ONBOARDING"
    END = "END"

class Candidate(TypedDict):
    id: str
    name: str
    email: str
    status: str

class HiringState(TypedDict):
    job_id: str
    job_title: str
    jd_content: str
    status: str
    candidates: List[Candidate]
    enough_applicants: bool
    jd_approved: bool
    candidate_selected: bool
    offer_accepted: bool

# Node functions
def hiring_request(state: HiringState):
    print("--- Hiring Request Received ---")
    return {"status": HiringStatus.HIRING_REQUEST}

def create_jd(state: HiringState):
    print("--- Creating JD ---")
    return {"status": HiringStatus.CREATE_JD, "jd_content": f"JD for {state['job_title']}"}

def review_jd(state: HiringState):
    print("--- Reviewing JD ---")
    # Placeholder for actual review logic
    return {"jd_approved": True}

def post_jd(state: HiringState):
    print("--- JD Posted (Waiting 7 Days) ---")
    return {"status": HiringStatus.POST_JD}

def monitor_applications(state: HiringState):
    print("--- Monitoring Applications ---")
    # Placeholder logic
    return {"enough_applicants": True}

def modify_jd(state: HiringState):
    print("--- Modifying JD ---")
    return {"status": HiringStatus.MODIFY_JD}

def wait_48_hours(state: HiringState):
    print("--- Waiting 48 Hours ---")
    return {"status": HiringStatus.WAIT_48_HOURS}

def shortlist(state: HiringState):
    print("--- Shortlisting ---")
    return {"status": HiringStatus.SHORTLIST, "candidates": [{"id": "1", "name": "John Doe", "email": "john@example.com", "status": "shortlisted"}]}

def schedule_interview(state: HiringState):
    print("--- Scheduling Interview ---")
    return {"status": HiringStatus.SCHEDULE_INTERVIEW}

def conduct_interview(state: HiringState):
    print("--- Conducting Interview ---")
    return {"status": HiringStatus.CONDUCT_INTERVIEW}

def interview_feedback(state: HiringState):
    print("--- Processing Feedback ---")
    return {"candidate_selected": True}

def send_offer_letter(state: HiringState):
    print("--- Sending Offer ---")
    # Simulate acceptance after one renegotiation to avoid infinite loop
    offer_accepted = state.get("status") == HiringStatus.RENEGOTIATE
    return {"status": HiringStatus.SEND_OFFER_LETTER, "offer_accepted": offer_accepted}

def renegotiate(state: HiringState):
    print("--- Renegotiating ---")
    return {"status": HiringStatus.RENEGOTIATE}

def reject_email(state: HiringState):
    print("--- Sending Rejection ---")
    return {"status": HiringStatus.REJECT_EMAIL}

def onboarding(state: HiringState):
    print("--- Onboarding ---")
    return {"status": HiringStatus.ONBOARDING}

# Build Graph
workflow = StateGraph(HiringState)

# Add Nodes
workflow.add_node("hiring_request", hiring_request)
workflow.add_node("create_jd", create_jd)
workflow.add_node("review_jd", review_jd)
workflow.add_node("post_jd", post_jd)
workflow.add_node("monitor_applications", monitor_applications)
workflow.add_node("modify_jd", modify_jd)
workflow.add_node("wait_48_hours", wait_48_hours)
workflow.add_node("shortlist", shortlist)
workflow.add_node("schedule_interview", schedule_interview)
workflow.add_node("conduct_interview", conduct_interview)
workflow.add_node("interview_feedback", interview_feedback)
workflow.add_node("send_offer_letter", send_offer_letter)
workflow.add_node("renegotiate", renegotiate)
workflow.add_node("reject_email", reject_email)
workflow.add_node("onboarding", onboarding)

# Set Entry Point
workflow.set_entry_point("hiring_request")

# Define Edges
workflow.add_edge("hiring_request", "create_jd")
workflow.add_edge("create_jd", "review_jd")

workflow.add_conditional_edges(
    "review_jd",
    lambda x: "approved" if x["jd_approved"] else "rejected",
    {
        "approved": "post_jd",
        "rejected": "create_jd"
    }
)

workflow.add_edge("post_jd", "monitor_applications")

workflow.add_conditional_edges(
    "monitor_applications",
    lambda x: "yes" if x["enough_applicants"] else "no",
    {
        "yes": "shortlist",
        "no": "modify_jd"
    }
)

workflow.add_edge("modify_jd", "wait_48_hours")
workflow.add_edge("wait_48_hours", "monitor_applications")
workflow.add_edge("shortlist", "schedule_interview")
workflow.add_edge("schedule_interview", "conduct_interview")
workflow.add_edge("conduct_interview", "interview_feedback")

workflow.add_conditional_edges(
    "interview_feedback",
    lambda x: "selected" if x["candidate_selected"] else "rejected",
    {
        "selected": "send_offer_letter",
        "rejected": "reject_email"
    }
)

workflow.add_conditional_edges(
    "send_offer_letter",
    lambda x: "accepted" if x.get("offer_accepted", True) else "renegotiate",
    {
        "accepted": "onboarding",
        "renegotiate": "renegotiate"
    }
)

workflow.add_edge("renegotiate", "send_offer_letter")
workflow.add_edge("reject_email", END)
workflow.add_edge("onboarding", END)

# Compile
app = workflow.compile()

# Test Run
if __name__ == "__main__":
    inputs = {
        "job_id": "JOB-001",
        "job_title": "Senior AI Engineer",
        "jd_content": "",
        "status": HiringStatus.START,
        "candidates": [],
        "enough_applicants": False,
        "jd_approved": False,
        "candidate_selected": False,
        "offer_accepted": False
    }
    for output in app.stream(inputs):
        for key, value in output.items():
            print(f"Node '{key}' completed.")
