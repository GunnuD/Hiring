import { HiringStatus } from './types.js';
export class HiringTool {
    state;
    constructor(jobId, jobTitle) {
        this.state = {
            jobId,
            jobTitle,
            jdContent: '',
            status: HiringStatus.START,
            candidates: []
        };
        console.log(`Starting hiring workflow for: ${jobTitle} (${jobId})`);
    }
    async process() {
        console.log(`Current state: ${this.state.status}`);
        switch (this.state.status) {
            case HiringStatus.START:
                this.hiringRequest();
                break;
            case HiringStatus.HIRING_REQUEST:
                this.createJD();
                break;
            case HiringStatus.CREATE_JD:
                this.reviewJD();
                break;
            case HiringStatus.POST_JD:
                await this.wait7Days();
                break;
            case HiringStatus.MONITOR_APPLICATIONS:
                this.monitorApplications();
                break;
            case HiringStatus.MODIFY_JD:
                this.modifyJD();
                break;
            case HiringStatus.WAIT_48_HOURS:
                await this.wait48Hours();
                break;
            case HiringStatus.SHORTLIST:
                this.shortlistCandidates();
                break;
            case HiringStatus.SCHEDULE_INTERVIEW:
                this.scheduleInterview();
                break;
            case HiringStatus.CONDUCT_INTERVIEW:
                this.conductInterview();
                break;
            case HiringStatus.INTERVIEW_FEEDBACK:
                this.interviewFeedback();
                break;
            case HiringStatus.SEND_OFFER_LETTER:
                this.sendOfferLetter();
                break;
            case HiringStatus.RENEGOTIATE:
                this.renegotiate();
                break;
            case HiringStatus.ONBOARDING:
                this.onboarding();
                break;
            case HiringStatus.REJECT_EMAIL:
                this.rejectEmail();
                break;
            case HiringStatus.END:
                console.log('Workflow completed.');
                break;
            default:
                console.log(`Unhandled status: ${this.state.status}`);
        }
    }
    hiringRequest() {
        console.log('Step: Hiring Request received.');
        this.state.status = HiringStatus.HIRING_REQUEST;
        this.process();
    }
    createJD() {
        console.log('Step: Creating Job Description.');
        this.state.jdContent = `Job Description for ${this.state.jobTitle}`;
        this.state.status = HiringStatus.CREATE_JD;
        this.process();
    }
    reviewJD() {
        console.log('Step: Reviewing JD.');
        const approved = true; // Placeholder for logic
        if (approved) {
            console.log('JD Approved.');
            this.state.status = HiringStatus.POST_JD;
        }
        else {
            console.log('JD Rejected, recreating...');
            this.state.status = HiringStatus.CREATE_JD;
        }
        this.process();
    }
    async wait7Days() {
        console.log('Step: Posting JD and waiting 7 days for applications...');
        // Simulated wait
        this.state.status = HiringStatus.MONITOR_APPLICATIONS;
        this.process();
    }
    monitorApplications() {
        console.log('Step: Monitoring Applications.');
        const enoughApplicants = true; // Placeholder logic
        if (enoughApplicants) {
            this.state.status = HiringStatus.SHORTLIST;
        }
        else {
            this.state.status = HiringStatus.MODIFY_JD;
        }
        this.process();
    }
    modifyJD() {
        console.log('Step: Modifying JD.');
        this.state.status = HiringStatus.WAIT_48_HOURS;
        this.process();
    }
    async wait48Hours() {
        console.log('Step: Waiting 48 hours after JD modification...');
        this.state.status = HiringStatus.MONITOR_APPLICATIONS;
        this.process();
    }
    shortlistCandidates() {
        console.log('Step: Shortlisting Candidates.');
        // Simulate finding a candidate
        this.state.candidates.push({
            id: '1',
            name: 'John Doe',
            email: 'john@example.com',
            status: HiringStatus.SHORTLIST
        });
        this.state.status = HiringStatus.SCHEDULE_INTERVIEW;
        this.process();
    }
    scheduleInterview() {
        console.log('Step: Scheduling Interview.');
        this.state.status = HiringStatus.CONDUCT_INTERVIEW;
        this.process();
    }
    conductInterview() {
        console.log('Step: Conducting Interview.');
        this.state.status = HiringStatus.INTERVIEW_FEEDBACK;
        this.process();
    }
    interviewFeedback() {
        console.log('Step: Processing Interview Feedback.');
        const selected = true; // Placeholder logic
        if (selected) {
            this.state.status = HiringStatus.SEND_OFFER_LETTER;
        }
        else {
            this.state.status = HiringStatus.REJECT_EMAIL;
        }
        this.process();
    }
    rejectEmail() {
        console.log('Step: Sending Rejection Email.');
        this.state.status = HiringStatus.END;
        this.process();
    }
    sendOfferLetter() {
        console.log('Step: Sending Offer Letter.');
        const accepted = true; // Placeholder logic
        if (accepted) {
            this.state.status = HiringStatus.ONBOARDING;
        }
        else {
            this.state.status = HiringStatus.RENEGOTIATE;
        }
        this.process();
    }
    renegotiate() {
        console.log('Step: Renegotiating offer.');
        // After renegotiation, send offer again
        this.state.status = HiringStatus.SEND_OFFER_LETTER;
        this.process();
    }
    onboarding() {
        console.log('Step: Onboarding new hire.');
        this.state.status = HiringStatus.END;
        this.process();
    }
    getStatus() {
        return this.state.status;
    }
}
//# sourceMappingURL=index.js.map