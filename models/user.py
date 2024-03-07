from sqlalchemy import Column, Integer, String
from models import database


class Users(database.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)


def get_user_by_email_and_password(session, email, password):
    return session.query(Users).filter(
        Users.email == email,
        Users.password == password
    ).first()
