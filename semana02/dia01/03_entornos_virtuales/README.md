# Entornos virtuales

## ¿Qué es un entorno virtual?
Un entorno virtual es una herramienta que nos permite crear un entorno de desarrollo aislado del sistema principal. Esto nos permite instalar las dependicas necesarias para nuestro proyecto sin afectar a otros proyectos que tengamos en el mismo sistema.

## Crear un entorno virtual

```bash
python -m venv nombre_entorno_virtual
```

## Activar un entorno virtual

```bash
# Windows cmd o powershell
nombre_entorno_virtual\Scripts\activate

# Git Bash
source nombre_entorno_virtual/Scripts/activate

# MacOS o Linux
source nombre_entorno_virtual/bin/activate
```

## Desactivar un entorno virtual

```bash
deactivate
```

## Instalar dependencias

```bash
pip install Flask
```

## Desinstalar dependencias

```bash
pip uninstall Flask
```

## Lista de dependencias

```bash
pip list
pip freeze
pip freeze > requirements.txt # Exportar dependencias
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```