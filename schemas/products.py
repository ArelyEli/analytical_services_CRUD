from pydantic import BaseModel

class CreateNewProductRequest(BaseModel):
    name: str
    description: str
    price: float
    stock: int
