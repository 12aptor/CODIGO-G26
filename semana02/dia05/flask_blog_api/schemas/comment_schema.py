from pydantic import BaseModel, Field


class CommentSchema(BaseModel):
    content: str = Field(..., min_length=1, max_length=1000)
    post_id: int
    author_id: int