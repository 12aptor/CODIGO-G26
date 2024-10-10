# Django Rest Framework

## Instalación

```bash
pip install Django
pip install djangorestframework
pip install python-dotenv
pip install psycopg2-binary
```

## Creación del proyecto

```bash
django-admin startproject django_rest_framework .
```

## Configuración

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    ...
]
```

## Variables de entorno

```bash
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_HOST=''
DB_PORT=''
```