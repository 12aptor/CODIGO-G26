from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, Boolean, DateTime
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(200))
    password: Mapped[str] = mapped_column(Text)
    status: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'status': self.status,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }