from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.dto.auth import (
    RegisterUserDTO,
    RegisterUserResponseDTO,
    LoginUserDTO,
    LoginResponseDTO,
)
from app.services.auth import(
    register_user,
    login_user,
)

from app.dependencies import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


##def get_db():
  ##  db = SessionLocal()

    ##try:
      ##  yield db
    ##finally:
      ##  db.close()


@router.post(
    "/register",
    response_model=RegisterUserResponseDTO,
)
def register(
    payload: RegisterUserDTO,
    db: Session = Depends(get_db),
):
    return register_user(
        db=db,
        payload=payload,
    )



@router.post(
    "/login",
    response_model=LoginResponseDTO,
)
def login(
    payload: LoginUserDTO,
    db: Session = Depends(get_db),
):
    return login_user(
        db=db,
        payload=payload,
    )