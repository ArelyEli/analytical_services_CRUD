from sqlalchemy import FLOAT, Column, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column

from models import database
from models.user import Users


class Products(database.Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    description = Column(String)
    price = Column(FLOAT)
    stock = Column(Integer)
    user_id = mapped_column(ForeignKey("users.id"))

    def __repr__(self):
        return self.name


def get_product_by_name(session, name):
    return session.query(Products).filter(Products.name == name).first()


def get_product_by_id(session, product_id):
    return session.query(Products).filter(Products.id == product_id).first()


def delete_product_by_id(session, product_id):
    session.query(Products).filter(Products.id == product_id).delete()
    session.commit()


def update_product_by_id(session, product_id, new_values):
    new_values_filtered = {
        key: value for key, value in new_values.items() if value is not None
    }
    print(new_values, new_values_filtered)
    session.query(Products).filter(Products.id == product_id).update(
        new_values_filtered
    )
    session.commit()


def create_new_product(session, product, user: Users):
    new_product = Products(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock,
        user_id=user.id,
    )

    session.add(new_product)
    session.commit()


def get_products(session):
    return session.query(Products).all()
