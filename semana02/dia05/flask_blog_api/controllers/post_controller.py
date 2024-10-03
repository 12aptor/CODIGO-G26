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

            try:
                json['author_id'] = int(json.get('author_id'))
            except:
                json['author_id'] = json.get('author_id')
            
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
        
    def list(self):
        try:
            post = self.model.query.all()

            return {
                'message': 'Listado de posts',
                'data': [post.to_dict() for post in post]
            }
        except Exception as e:
            return {
                'message': ' Error al obtener los posts',
                'error': str(e)
            }, 500
        
    def get_by_id(self, id):
        try:
            post = self.model.query.get(id)

            if not post:
                return {
                    'message': 'El post no existe'
                }, 404
            
            return {
                'message': 'Post obtenido correctamente',
                'data': post.to_dict()
            }, 200
        except Exception as e:
            return {
                'message': 'Error al obtener el post',
                'error': str(e)
            }, 500