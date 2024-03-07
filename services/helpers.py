from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from models.user import get_user_by_email
from models.product import get_product_by_name
from fastapi import HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from schemas.user import User
from models.database import Session

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict):
    to_encode = data.copy()
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def is_user_in_db(session, email) -> bool:
    user = get_user_by_email(session, email)
    return bool(user)


def is_product_in_db(session, name) -> bool:
    user = get_product_by_name(session, name)
    return bool(user)


def get_user_by_jwt(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    session = Session()
    user = get_user_by_email(session, email)
    session.close()
    if user is None:
        raise credentials_exception
    return User(
        id=user.id,
        email=user.email,
        username=user.username,
    )
