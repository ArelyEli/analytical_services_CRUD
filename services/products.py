from services.helpers import is_product_in_db
from models.product import create_new_product, get_products, get_product_by_id, delete_product_by_id, update_product_by_id, get_product_by_name
from services.errors import ProducAlreadyExistError, ProducNotFoundError
from schemas.products import Product, GetAllProductsResponse

def create_product(session, product, user):
    if is_product_in_db(session, product.name):
        raise ProducAlreadyExistError()
    
    create_new_product(session, product, user)

def get_all_products(session):
    products = get_products(session)

    products = [Product(
        id = product.id,
        name = product.name,
        description = product.description,
        price = product.price,
        stock = product.stock
    ) for product in products]

    return GetAllProductsResponse(
        products = products
    )


def get_a_product(session, product_id):
    product = get_product_by_id(session, product_id)

    if not product:
        raise ProducNotFoundError()

    return Product(
        id = product.id,
        name = product.name,
        description = product.description,
        price = product.price,
        stock = product.stock
    )


def delete_a_product(session, product_id):
    product = get_product_by_id(session, product_id)

    if not product:
        raise ProducNotFoundError()

    delete_product_by_id(session, product_id)

def update_a_product(session, product_id, new_values):
    product = get_product_by_id(session, product_id)
    if not product:
        raise ProducNotFoundError()

    product = get_product_by_name(session, new_values['name'])
    if product:
        raise ProducAlreadyExistError()

    update_product_by_id(session, product_id, new_values)