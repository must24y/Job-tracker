export interface JobApplication {
  id: string;
  company_name: string;
  job_title: string;
  job_description: string | null;
  job_url: string | null;
  location: string | null;
  source: string | null;
  resume_used: string | null;
  email_used: string | null;
  phone_used: string | null;
  date_applied: string | null;
  deadline: string | null;
  status: string;
  notes: string | null;
}


export interface JobApplicationListResponse {
  items: JobApplication[];
  page: number;
  page_size: number;
  total: number;
  total_pages: number;
}

export interface ApplicationFilters {
  company_name?: string;
  job_title?: string;
  resume_used?: string;
  source?: string;
  status?: string;
  page?: number;
  page_size?: number;
}