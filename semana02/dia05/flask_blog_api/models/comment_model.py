from db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, ForeignKey
from datetime import datetime
from models.user_model import UserModel


class CommentModel(db.Model):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str]
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.now)
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    author: Mapped[UserModel] = relationship(back_populates='comments')