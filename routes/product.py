from typing import Annotated
from fastapi import Depends
from fastapi import HTTPException, status
from typing import Annotated
from schemas.core import MessageResponse
from schemas.products import CreateNewProductRequest, GetAllProductsResponse
from sqlalchemy.orm.session import Session
from models.database import get_session
from fastapi import APIRouter
from schemas.user import User
from services.helpers import get_user_by_jwt
from services.products import create_product, get_all_products
from services.errors import ProducAlreadyExistError

product_router = APIRouter(
    tags=['products']
)

@product_router.post("/products")
async def handler_create_product(
    user: Annotated[User, Depends(get_user_by_jwt)],
    product: CreateNewProductRequest,
    session: Session = Depends(get_session)
) -> MessageResponse:
    try:
        create_product(session, product, user)

        return MessageResponse(
            message = 'Product successfully added'
        )
    except ProducAlreadyExistError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@product_router.get("/products")
async def handler_create_product(
    session: Session = Depends(get_session)
) -> GetAllProductsResponse:
    try:
        products = get_all_products(session)

        return products
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
