from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from schemas.auth import LoginResponse
from services.auth import login
from sqlalchemy.orm.session import Session
from models.database import get_session
from fastapi import APIRouter

auth_router = APIRouter()

@auth_router.post("/login")
async def handler_login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Session = Depends(get_session)
) -> LoginResponse:
    token = login(session, form_data.username, form_data.password)

    return LoginResponse(
        access_token = token
    )
