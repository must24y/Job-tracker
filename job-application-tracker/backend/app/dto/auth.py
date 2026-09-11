from uuid import UUID

from pydantic import BaseModel, EmailStr


class RegisterUserDTO(BaseModel):
    name: str
    email: EmailStr
    password: str
    default_email: EmailStr | None = None
    default_phone: str | None = None


class RegisterUserResponseDTO(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    default_email: EmailStr | None
    default_phone: str | None

    model_config = {
        "from_attributes": True
    }



class LoginUserDTO(BaseModel):
    email: EmailStr
    password: str


class LoginResponseDTO(BaseModel):
    access_token: str
    token_type: str