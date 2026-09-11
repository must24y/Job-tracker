from passlib.context import CryptContext

from datetime import datetime, timedelta, timezone

from jose import jwt

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    password_hash: str,
) -> bool:
    return pwd_context.verify(
        plain_password,
        password_hash,
    )


SECRET_KEY = "this is going@@@%@%^wsfwe4&*%()tobemyfirstownjwtcode"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(user_id: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": user_id,
        "exp": expire,
    }##expiration also in payload

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )