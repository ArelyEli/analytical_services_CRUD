from pydantic import BaseModel
from typing import List

class CreateNewProductRequest(BaseModel):
    name: str
    description: str
    price: float
    stock: int

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int

class GetAllProductsResponse(BaseModel):
    products: List[Product] = []
