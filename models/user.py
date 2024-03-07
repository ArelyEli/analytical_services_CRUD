from sqlalchemy import Column, Integer, String
from models import database


class Users(database.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    def __repr__(self):
        return self.username


def get_user_by_email(session, email):
    return session.query(Users).filter(Users.email == email).first()


def create_new_user(session, email, hashed_password, username):
    new_user = Users(
        username=username,
        email=email,
        password=hashed_password,
    )

    session.add(new_user)
    session.commit()
