# Blog API

## Dependencias

```bash
pip install Flask # Framework
pip install Flask-SQLAlchemy # ORM
pip install Flask-Migrate # Migraciones
pip install Flask-Cors # CORS
pip install psycopg2-binary # PostgreSQL
pip install pydantic # Validacion de datos
pip install bcrypt # Hashing
pip install python-dotenv # Variable de entorno
pip install flask-jwt-extended # Autenticacion
pip install cloudinary # Almacenamiento de imágenes
pip install pytest # Tests
```

## Migraciones

```bash
# Crear la carpeta de migraciones (Se ejecuta una sola vez)
flask db init

# Crear la migracion
flask db migrate -m "Descripcion de la migracion"

# Aplicar la migracion
flask db upgrade
```

## Variables de entorno

```bash
DATABASE_URI=''
SECRET_KEY=''
CLOUDINARY_CLOUD_NAME=''
CLOUDINARY_API_KEY=''
CLOUDINARY_API_SECRET=''
```
