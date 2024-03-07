from models.user import get_user_by_email_and_password
from fastapi import HTTPException, status
from services.helpers import create_access_token
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def login(session, email, password):
    hashed_password = pwd_context.hash(password)
    user = get_user_by_email_and_password(session, email, hashed_password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return create_access_token(data={"sub": user.username})
