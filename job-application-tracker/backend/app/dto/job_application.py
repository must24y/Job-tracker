from datetime import date
from pydantic import BaseModel, EmailStr,Field
from uuid import UUID


class CreateJobApplicationDTO(BaseModel):
    company_name: str
    job_title: str
    job_description: str | None = None
    job_url: str | None = None
    location: str | None = None
    source: str | None = None
    resume_used: str | None = None
    email_used: EmailStr | None = None
    phone_used: str | None = None
    date_applied: date | None = None
    deadline: date | None = None
    status: str = "APPLIED"
    notes: str | None = None

## for searching and filtering this will be the request dto
##you must mention what all you will need for searching

class SearchJobApplicationsDTO(BaseModel):
    company_name: str | None = None
    job_title: str | None = None
    resume_used: str | None = None
    source: str | None = None
    status: str | None = None

    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=10, ge=1, le=100)


class JobApplicationResponseDTO(BaseModel):
    id: UUID ##sohereilearntthatfortheresponsemodel_validatenmsshldbesame
  ##butonlyforifyouareusingmodel_vlaidate
    company_name: str
    job_title: str
    job_description: str | None
    job_url: str | None
    location: str | None
    source: str | None
    resume_used: str | None
    email_used: str | None
    phone_used: str | None
    date_applied: date | None
    deadline: date | None
    status: str
    notes: str | None

    model_config = {
        "from_attributes": True
    }


class JobApplicationListResponseDTO(BaseModel):
    items: list[JobApplicationResponseDTO]
    page: int
    page_size: int
    total: int
    total_pages: int