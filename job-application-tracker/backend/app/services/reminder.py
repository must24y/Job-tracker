from uuid import UUID

from sqlalchemy.orm import Session

from app.dto.reminder import (
    CreateReminderDTO,
    ReminderResponseDTO,
)
from app.models.reminder import Reminder


import math

from app.dto.reminder import (
    SearchReminderDTO,
    ReminderListResponseDTO,
    ReminderResponseDTO,
)


def create_reminder(
    db: Session,
    user_id: UUID,
    payload: CreateReminderDTO,
) -> ReminderResponseDTO:

    reminder = Reminder(
        user_id=user_id,
        company_name=payload.company_name,
        job_title=payload.job_title,
        job_url=payload.job_url,
        job_description=payload.job_description,
        source=payload.source,
        deadline=payload.deadline,
        reminder_date=payload.reminder_date,
        notes=payload.notes,
    )

    db.add(reminder)
    db.commit()
    db.refresh(reminder)

    return ReminderResponseDTO.model_validate(reminder)


def get_reminders(
    db: Session,
    user_id,
    filters: SearchReminderDTO,
) -> ReminderListResponseDTO:

    query = (
        db.query(Reminder)
        .filter(Reminder.user_id == user_id)
    )

    if filters.company_name:
        query = query.filter(
            Reminder.company_name.ilike(
                f"%{filters.company_name}%"
            )
        )

    if filters.job_title:
        query = query.filter(
            Reminder.job_title.ilike(
                f"%{filters.job_title}%"
            )
        )

    if filters.source:
        query = query.filter(
            Reminder.source == filters.source
        )

    total = query.count()

    offset = (filters.page - 1) * filters.page_size

    reminders = (
        query
        .offset(offset)
        .limit(filters.page_size)
        .all()
    )

    total_pages = math.ceil(
        total / filters.page_size
    )

    items = [
        ReminderResponseDTO.model_validate(reminder)
        for reminder in reminders
    ]

    return ReminderListResponseDTO(
        items=items,
        page=filters.page,
        page_size=filters.page_size,
        total=total,
        total_pages=total_pages,
    )