from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.dto.auth import (
    RegisterUserDTO,
    RegisterUserResponseDTO,
)
from app.models.user import User
from app.security import hash_password,verify_password

from app.dto.auth import(
    LoginUserDTO,
    LoginResponseDTO
)

from app.security import create_access_token

def register_user(
    db: Session,
    payload: RegisterUserDTO,
) -> RegisterUserResponseDTO:

    existing_user = (
        db.query(User)
        .filter(User.email == payload.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email is already registered",
        )

    hashed_password = hash_password(payload.password)

    user = User(
        name=payload.name,
        email=payload.email,
        password_hash=hashed_password,
        default_email=payload.default_email,
        default_phone=payload.default_phone,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return RegisterUserResponseDTO.model_validate(user)



def login_user(
    db: Session,
    payload: LoginUserDTO,
) -> LoginResponseDTO:

    user = (
        db.query(User)
        .filter(User.email == payload.email)
        .first()
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    password_valid = verify_password(
        payload.password,
        user.password_hash,
    )

    if not password_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        str(user.id)
    )

    return LoginResponseDTO(
        access_token=access_token,
        token_type="bearer",
    )