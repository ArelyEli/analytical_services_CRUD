from fastapi import HTTPException, status
from services.helpers import is_product_in_db
from models.product import create_new_product
from services.errors import ProducAlreadyExistError

def create_product(session, product, user):
    if is_product_in_db(session, product.name):
        raise ProducAlreadyExistError()
    
    create_new_product(session, product, user)
