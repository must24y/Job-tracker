from datetime import date
from uuid import UUID

from pydantic import BaseModel,Field


class CreateReminderDTO(BaseModel):
    company_name: str
    job_title: str
    job_url: str | None = None
    job_description: str | None = None
    source: str | None = None
    deadline: date | None = None
    remind_at: date | None = None
    notes: str | None = None


class ReminderResponseDTO(BaseModel):
    id: UUID
    company_name: str
    job_title: str
    job_url: str | None
    job_description: str | None
    source: str | None
    deadline: date | None
    remind_at: date | None
    notes: str | None

    model_config = {
        "from_attributes": True
    }



class SearchReminderDTO(BaseModel):
    company_name: str | None = None
    job_title: str | None = None
    source: str | None = None

    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=10, ge=1, le=100)


class ReminderListResponseDTO(BaseModel):
    items: list[ReminderResponseDTO]
    page: int
    page_size: int
    total: int
    total_pages: int



class UpdateReminderDTO(BaseModel):
    company_name: str | None = None
    job_title: str | None = None
    job_url: str | None = None
    job_description: str | None = None
    source: str | None = None
    deadline: date | None = None
    remind_at: date | None = None
    notes: str | None = None