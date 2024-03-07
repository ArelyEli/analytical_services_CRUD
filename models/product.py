from sqlalchemy import Column, Integer, String, FLOAT, ForeignKey
from sqlalchemy.orm import mapped_column
from models import database
from models.user import Users


class Products(database.Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    price = Column(FLOAT)
    stock = Column(Integer)
    user_id = mapped_column(ForeignKey("users.id"))

    def __repr__(self):
        return self.name

def get_product_by_name(session, name):
    return session.query(Products).filter(
        Products.name == name
    ).first()


def create_new_product(session, product, user: Users):
    new_product = Products(
        name = product.name,
        description = product.description,
        price = product.price,
        stock = product.stock,
        user_id = user.id,
    )

    session.add(new_product)
    session.commit()
