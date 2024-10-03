from models.comment_model import CommentModel
from schemas.comment_schema import CommentSchema
from pydantic import ValidationError
from db import db


class CommentController:
    def __init__(self):
        self.model = CommentModel

    def create(self, json):
        try:
            validated_comment = CommentSchema.model_validate(json, strict=True)

            comment = self.model(**validated_comment.model_dump())

            db.session.add(comment)
            db.session.commit()

            return {
                'message': 'Comentario creado correctamente',
                'data': comment.to_dict()
            }, 201
        except ValidationError as e:
            return {
                'message': 'Error al validar el comentario',
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'message': 'Error al crear el comentario',
                'error': str(e)
            }, 500