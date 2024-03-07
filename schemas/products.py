from pydantic import BaseModel
from typing import List
from typing import Optional


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


class ProductToUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None

    def as_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
        }


class GetAllProductsResponse(BaseModel):
    products: List[Product] = []
