from sqlalchemy.orm import Session

from app.models.job_application import JobApplication
from app.dto.job_application import CreateJobApplicationDTO


import math

from sqlalchemy.orm import Session

from app.models.job_application import JobApplication
from app.dto.job_application import (
    SearchJobApplicationsDTO,
    JobApplicationListResponseDTO,
    JobApplicationResponseDTO,
)



def create_job_application(
    db: Session,
    payload: CreateJobApplicationDTO,
    user_id
) -> JobApplication:

    application = JobApplication(
        user_id=user_id,
        company_name=payload.company_name,
        job_title=payload.job_title,
        job_description=payload.job_description,
        job_url=payload.job_url,
        location=payload.location,
        source=payload.source,
        resume_used=payload.resume_used,
        email_used=payload.email_used,
        phone_used=payload.phone_used,
        date_applied=payload.date_applied,
        deadline=payload.deadline,
        status=payload.status,
        notes=payload.notes,
    )

    db.add(application)
    db.commit()
    db.refresh(application)

    return application



def search_job_applications(
    db: Session,
    user_id,
    filters: SearchJobApplicationsDTO,
) -> JobApplicationListResponseDTO:

    query = db.query(JobApplication).filter(
        JobApplication.user_id == user_id
    )

    if filters.company_name:
        query = query.filter(
            JobApplication.company_name.ilike(
                f"%{filters.company_name}%"
            )
        )

    if filters.job_title:
        query = query.filter(
            JobApplication.job_title.ilike(
                f"%{filters.job_title}%"
            )
        )

    if filters.resume_used:
        query = query.filter(
            JobApplication.resume_used == filters.resume_used
        )

    if filters.source:
        query = query.filter(
            JobApplication.source == filters.source
        )

    if filters.status:
        query = query.filter(
            JobApplication.status == filters.status
        )

    total = query.count()

    offset = (filters.page - 1) * filters.page_size

    applications = (
        query
        .offset(offset)
        .limit(filters.page_size)
        .all()
    )

    total_pages = math.ceil(total / filters.page_size)

    items = [
        JobApplicationResponseDTO.model_validate(application)
        for application in applications
    ]

    return JobApplicationListResponseDTO(
        items=items,
        page=filters.page,
        page_size=filters.page_size,
        total=total,
        total_pages=total_pages,
    )