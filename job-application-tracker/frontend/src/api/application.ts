import { apiClient } from "./client";

import type {
  ApplicationFilters,
  JobApplicationListResponse,
} from "../types/application";

export async function getApplications(
  filters: ApplicationFilters = {},
): Promise<JobApplicationListResponse> {
  const params = new URLSearchParams();

  if (filters.company_name) {
    params.set("company_name", filters.company_name);
  }

  if (filters.job_title) {
    params.set("job_title", filters.job_title);
  }

  if (filters.resume_used) {
    params.set("resume_used", filters.resume_used);
  }

  if (filters.source) {
    params.set("source", filters.source);
  }

  if (filters.status) {
    params.set("status", filters.status);
  }

  params.set(
    "page",
    String(filters.page ?? 1),
  );

  params.set(
    "page_size",
    String(filters.page_size ?? 10),
  );

  return apiClient<JobApplicationListResponse>(
    `/applications/?${params.toString()}`,
    {
      method: "GET",
      requiresAuth: true,
    },
  );
}