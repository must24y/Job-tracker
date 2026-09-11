from uuid import UUID

from fastapi import Depends, HTTPException, status
##from fastapi.security import OAuth2PasswordBearer
##thisoneuserdifferentformatsowegowtihhttpbearer

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from app.security import SECRET_KEY, ALGORITHM


##oauth2_scheme = OAuth2PasswordBearer(
  ##  tokenUrl="/auth/login"
##)

bearer_scheme = HTTPBearer()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_current_user(
    ##token: str = Depends(oauth2_scheme),
    credentials:HTTPAuthorizationCredentials=Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> User:

    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

    user_id = payload.get("sub")

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

    try:
        user_id = UUID(user_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

    return user



"""
OAuth2
   ↓
The authentication/authorization convention

OAuth2PasswordBearer
   ↓
FastAPI security helper that extracts a Bearer
token from the Authorization header and describes
the OAuth2 password flow

tokenUrl="/auth/login"
   ↓
Tells FastAPI/OpenAPI where the client obtains
the access token

JWT
   ↓
The actual token format we're generating

Bearer
   ↓
How the client presents that token"""