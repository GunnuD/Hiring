import { HiringStatus } from './types.js';
export declare class HiringTool {
    private state;
    constructor(jobId: string, jobTitle: string);
    process(): Promise<void>;
    private hiringRequest;
    private createJD;
    private reviewJD;
    private wait7Days;
    private monitorApplications;
    private modifyJD;
    private wait48Hours;
    private shortlistCandidates;
    private scheduleInterview;
    private conductInterview;
    private interviewFeedback;
    private rejectEmail;
    private sendOfferLetter;
    private renegotiate;
    private onboarding;
    getStatus(): HiringStatus;
}
//# sourceMappingURL=index.d.ts.map