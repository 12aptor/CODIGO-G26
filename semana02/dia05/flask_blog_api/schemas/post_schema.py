from pydantic import BaseModel


class PostSchema(BaseModel):
    title: str
    content: str
    image: str
    author_id: int