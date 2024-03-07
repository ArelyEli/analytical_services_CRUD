from models.user import create_new_user, get_user_by_email
from fastapi import HTTPException, status
from services.helpers import create_access_token, is_user_in_db
from passlib.context import CryptContext
from schemas.auth import SignUpRequest

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def login(session, email, password):
    user = get_user_by_email(session, email)

    print(user)

    is_valid = pwd_context.verify(password, user.password)

    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return create_access_token(data={"sub": user.email})

def signup(session, user_info: SignUpRequest):
    if is_user_in_db(session, user_info.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    hashed_password = pwd_context.hash(user_info.password)

    create_new_user(session, user_info.email, hashed_password, user_info.username)
