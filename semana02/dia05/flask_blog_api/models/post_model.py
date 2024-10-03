from db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, DateTime, ForeignKey
from datetime import datetime
from models.user_model import UserModel
from models.comment_model import CommentModel
import cloudinary_config
import cloudinary.utils
from typing import List


class PostModel(db.Model):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    content: Mapped[str] = mapped_column(Text)
    image: Mapped[str] = mapped_column(Text)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    author: Mapped[UserModel] = relationship()
    comments: Mapped[List[CommentModel]] = relationship()


    def to_dict(self, image_url=None):
        if image_url is None:
            image_url = cloudinary.utils.cloudinary_url(self.image)[0]

        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'image': image_url,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
            'author_id': self.author_id,
            'author': self.author.to_dict(),
            'comments': [comment.to_dict() for comment in self.comments]
        }