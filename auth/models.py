from typing import Optional, Annotated
from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database_main.database import Base


intpk = Annotated[int, mapped_column(primary_key=True)]


class UsersORM(Base):
    __tablename__ = 'users'

    id: Mapped[intpk]
    username: Mapped[str] =  mapped_column(String(25), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)


