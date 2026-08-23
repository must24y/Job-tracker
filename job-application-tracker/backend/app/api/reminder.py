from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.dto.reminder import (
    CreateReminderDTO,
    ReminderResponseDTO,
)
from app.services.reminder import create_reminder


from app.dto.reminder import (
    SearchReminderDTO,
    ReminderListResponseDTO,
)
from app.services.reminder import(
    get_reminders
)


router = APIRouter(
    prefix="/reminders",
    tags=["Reminders"],
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post(
    "/",
    response_model=ReminderResponseDTO,
)
def create_reminder_api(
    payload: CreateReminderDTO,
    db: Session = Depends(get_db),
):
    # Temporary until authentication is implemented
    user_id = None

    return create_reminder(
        db=db,
        user_id=user_id,
        payload=payload,
    )



@router.get(
    "/",
    response_model=ReminderListResponseDTO,
)
def get_reminder_list(
    db: Session = Depends(get_db),
    filters: SearchReminderDTO = Depends(),
):
    # Temporary until authentication is implemented
    user_id = None

    return get_reminders(
        db=db,
        user_id=user_id,
        filters=filters,
    )