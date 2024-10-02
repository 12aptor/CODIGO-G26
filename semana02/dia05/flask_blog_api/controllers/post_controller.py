from models.post_model import PostModel
from pydantic import ValidationError
from schemas.post_schema import PostSchema
from db import db
import cloudinary.uploader
from werkzeug.datastructures import FileStorage
import uuid


class PostController:
    def __init__(self):
        self.model = PostModel
    
    def create(self, json, image: FileStorage):
        try:
            if image is None:
                return {
                    'message': 'Se requiere una imagen'
                }, 400

            filename = image.filename.split('.')[0]
            public_id = f'{uuid.uuid4()}-{filename}'
            
            cloudinary_response = cloudinary.uploader.upload(
                image.stream,
                public_id=public_id
            )

            json['image'] = public_id

            json['author_id'] = int(json.get('author_id'))
            
            validated_post = PostSchema.model_validate(json, strict=True)

            post = self.model(**validated_post.model_dump())
            
            db.session.add(post)
            db.session.commit()

            return {
                'message': 'Post creado correctamente',
                'data': post.to_dict(cloudinary_response['secure_url'])
            }, 201
        except ValidationError as e:
            return {
                'message': 'Error al validar el post',
                'error': e.errors()
            }, 400
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Error al crear el post',
                'error': str(e)
            }, 500