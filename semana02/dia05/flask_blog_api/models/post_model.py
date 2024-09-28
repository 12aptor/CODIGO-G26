from db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, DateTime, ForeignKey
from datetime import datetime
from models.user_model import UserModel


class PostModel(db.Model):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    content: Mapped[str] = mapped_column(Text)
    image: Mapped[str] = mapped_column(Text)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    author: Mapped[UserModel] = relationship(back_populates='posts')