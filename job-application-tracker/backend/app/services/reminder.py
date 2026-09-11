from uuid import UUID

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.dto.reminder import (
    CreateReminderDTO,
    ReminderResponseDTO,
    SearchReminderDTO,
    ReminderListResponseDTO,
    UpdateReminderDTO,
)

from app.models.reminder import Reminder


import math


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
        remind_at=payload.remind_at,
        notes=payload.notes,
    )

    db.add(reminder)
    db.commit()
    db.refresh(reminder)

    return ReminderResponseDTO.model_validate(reminder)


def get_reminders(
    db: Session,
    user_id: UUID,
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



def update_reminder(
    db: Session,
    user_id: UUID,
    reminder_id: UUID,
    payload: UpdateReminderDTO,
) -> ReminderResponseDTO:

    reminder = (
        db.query(Reminder)
        .filter(
            Reminder.id == reminder_id,
            Reminder.user_id == user_id,
        )
        .first()
    )

    if reminder is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reminder not found",
        )

    update_data = payload.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(reminder, field, value)

    db.commit()
    db.refresh(reminder)

    return ReminderResponseDTO.model_validate(reminder)
    ##always remember we are not filling the response to update the
    ##db but the response is filled afeter the db is updated or
    ##filled through payload