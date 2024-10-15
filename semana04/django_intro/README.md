# Django Intro

## Instalar dependencias

```bash
pip install Django
```

## Crear un proyecto

```bash
django-admin startproject "nombre_proyecto" .
```

## Iniciar el servidor

```bash
python manage.py runserver
```

## Migraciones

```bash
python manage.py makemigrations # Crear las migraciones
python manage.py makemigrations nombre_de_la_aplicacion # Crear las migraciones de una aplicacion
python manage.py migrate # Ejecuta las migraciones
python manage.py showmigrations # Muestra las migraciones
```

## Crear un superusuario

```bash
python manage.py createsuperuser
```

## Crear una aplicación

```bash
python manage.py startapp almacen
```