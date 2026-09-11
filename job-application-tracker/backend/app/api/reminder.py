from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session



from app.dto.reminder import (
    CreateReminderDTO,
    ReminderResponseDTO,
    SearchReminderDTO,
    ReminderListResponseDTO,
    UpdateReminderDTO,
)

from app.services.reminder import (
    create_reminder,
    get_reminders,
    update_reminder,
)

from app.models.user import User 

from app.dependencies import get_db, get_current_user

from uuid import UUID 

router = APIRouter(
    prefix="/reminders",
    tags=["Reminders"],
)


@router.post(
    "/",
    response_model=ReminderResponseDTO,
)
def create_reminder_api(
    payload: CreateReminderDTO,
    db: Session = Depends(get_db),
    current_user: User= Depends(get_current_user)
):
    # Temporary until authentication is implemented
    ##user_id = None

    return create_reminder(
        db=db,
        user_id=current_user.id,
        payload=payload,
    )



@router.get(
    "/",
    response_model=ReminderListResponseDTO,
)
def get_reminder_list(
    db: Session = Depends(get_db),
    current_user: User= Depends(get_current_user),
    filters: SearchReminderDTO = Depends(),
):
    # Temporary until authentication is implemented
    ##user_id = None

    return get_reminders(
        db=db,
        user_id=current_user.id,
        filters=filters,
    )


@router.patch(
    "/{reminder_id}",
    response_model=ReminderResponseDTO,
)
def update_reminder_api(
    reminder_id: UUID,
    payload: UpdateReminderDTO,
    db: Session = Depends(get_db),
    current_user: User= Depends(get_current_user)
):
    # Temporary until authentication is implemented
    ##user_id = None

    return update_reminder(
        db=db,
        user_id=current_user.id,
        reminder_id=reminder_id,
        payload=payload,
    )