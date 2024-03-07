from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import HTTPException, status
from schemas.auth import LoginResponse, SignUpRequest, SignUpResponse
from services.auth import login, signup
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


@auth_router.post("/signup")
async def handler_signup(
    user_info: SignUpRequest,
    session: Session = Depends(get_session)
) -> SignUpResponse:
    try:
        signup(session, user_info)

        return SignUpResponse(
            message = 'Successful SignUp'
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )
