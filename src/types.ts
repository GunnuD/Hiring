export enum HiringStatus {
  START = 'START',
  HIRING_REQUEST = 'HIRING_REQUEST',
  CREATE_JD = 'CREATE_JD',
  REVIEW_JD = 'REVIEW_JD',
  POST_JD = 'POST_JD',
  WAIT_7_DAYS = 'WAIT_7_DAYS',
  MONITOR_APPLICATIONS = 'MONITOR_APPLICATIONS',
  SHORTLIST = 'SHORTLIST',
  MODIFY_JD = 'MODIFY_JD',
  WAIT_48_HOURS = 'WAIT_48_HOURS',
  SCHEDULE_INTERVIEW = 'SCHEDULE_INTERVIEW',
  CONDUCT_INTERVIEW = 'CONDUCT_INTERVIEW',
  INTERVIEW_FEEDBACK = 'INTERVIEW_FEEDBACK',
  REJECT_EMAIL = 'REJECT_EMAIL',
  SEND_OFFER_LETTER = 'SEND_OFFER_LETTER',
  OFFER_ACCEPTED = 'OFFER_ACCEPTED',
  RENEGOTIATE = 'RENEGOTIATE',
  ONBOARDING = 'ONBOARDING',
  END = 'END'
}

export interface Candidate {
  id: string;
  name: string;
  email: string;
  status: HiringStatus;
}

export interface HiringWorkflowState {
  jobId: string;
  jobTitle: string;
  jdContent: string;
  status: HiringStatus;
  candidates: Candidate[];
}
