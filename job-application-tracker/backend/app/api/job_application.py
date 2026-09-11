import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.dto.job_application import CreateJobApplicationDTO
from app.services.job_application import create_job_application


from app.dto.job_application import (
    SearchJobApplicationsDTO,
    JobApplicationListResponseDTO,
)
from app.services.job_application import search_job_applications

from app.models.user import User 

from app.dependencies import get_db, get_current_user

router = APIRouter(
    prefix="/applications",
    tags=["Job Applications"],
)




@router.post("/")
def create_application(
    payload: CreateJobApplicationDTO,
    db: Session = Depends(get_db),
    current_user:User = Depends(get_current_user)
):

##    user_id = uuid.UUID("PUT-TEST-USER-UUID-HERE")

    return create_job_application(
        db=db,
        payload=payload,
        user_id=current_user.id,
    )



#@router.get("/")
#def get_applications(
 #   pagination: GetJobApplicationsDTO = Depends(),
  #  db: Session = Depends(get_db),
   # current_user: User = Depends(get_current_user)
#):
    # Temporary placeholder until authentication is implemented
    #user_id = None

 #   return get_job_applications(
  #      db=db,
   #     user_id=current_user.id,
    #    pagination=pagination,
    #)



@router.get(
    "/",
    response_model=JobApplicationListResponseDTO,
)
def get_applications(
    db: Session = Depends(get_db),
    filters: SearchJobApplicationsDTO = Depends(),
    current_user: User= Depends(get_current_user)
):
    #user_id = None

    return search_job_applications(
        db=db,
        filters=filters,
        user_id=current_user.id,
    )