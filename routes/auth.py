from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException, status
from schemas.auth import LoginResponse, SignUpRequest
from schemas.core import MessageResponse
from services.auth import login, signup
from sqlalchemy.orm.session import Session
from models.database import get_session
from fastapi import APIRouter
from services.errors import EmailAlreadyRegisteredError

auth_router = APIRouter(tags=["auth"])


@auth_router.post("/token")
async def handler_login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Session = Depends(get_session),
) -> LoginResponse:
    token = login(session, form_data.username, form_data.password)

    return LoginResponse(access_token=token)


@auth_router.post("/signup")
async def handler_signup(
    user_info: SignUpRequest, session: Session = Depends(get_session)
) -> MessageResponse:
    try:
        signup(session, user_info)

        return MessageResponse(message="Successful SignUp")
    except EmailAlreadyRegisteredError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
