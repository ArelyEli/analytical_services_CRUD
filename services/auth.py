from models.user import create_new_user, get_user_by_email
from fastapi import HTTPException, status
from services.helpers import create_access_token, is_user_in_db
from passlib.context import CryptContext
from schemas.auth import SignUpRequest
from services.errors import EmailAlreadyRegisteredError

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def login(session, email, password):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = get_user_by_email(session, email)

    if not user:
        raise exception

    is_valid = pwd_context.verify(password, user.password)

    if not is_valid:
        raise exception

    return create_access_token(data={"sub": user.email})


def signup(session, user_info: SignUpRequest):
    if is_user_in_db(session, user_info.email):
        raise EmailAlreadyRegisteredError()
    hashed_password = pwd_context.hash(user_info.password)

    create_new_user(session, user_info.email, hashed_password, user_info.username)
