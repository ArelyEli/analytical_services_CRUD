from fastapi import FastAPI
from pydantic import BaseModel

from models import database
from routes.auth import auth_router
from routes.product import product_router


class TokenData(BaseModel):
    username: str | None = None


class Token(BaseModel):
    access_token: str
    token_type: str


app = FastAPI()

app.include_router(auth_router)
app.include_router(product_router)

database.Base.metadata.create_all(database.engine)
