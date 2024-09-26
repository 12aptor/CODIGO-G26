# POSTGRESQL

## Crear tabla

```sql
CREATE TABLE movies (
	id SERIAL PRIMARY KEY,
	title VARCHAR(100),
	director VARCHAR(100),
	year INT,
	length_minutes INT
);
```

## Insertar registros

```sql
INSERT INTO movies (title, director, year, length_minutes)
VALUES
('Toy Story', 'John Lasseter', 1995, 81),
('Finding Nemo', 'Adrew Stanton', 2003, 100),
('The Incredibles', 'Brad Bird', 2004, 115),
('Ratatouille', 'Brad Bird', 2007, 111),
('Up', 'Pete Docter', 2009, 96),
('Toy Story 3', 'Lee Unkrich', 2010, 103),
('Inside Out', 'Pete Docter', 2015, 95),
('Coco', 'Lee Unkrich', 2017, 105),
('Toy Story 4', 'Josh Cooley', 2019, 100),
('Soul', 'Pete Docter', 2020, 100);
```

## SELECT

```sql
-- Seleccionar todos los registros
SELECT * FROM movies;

-- Sekeccuibar campos especificos
SELECT title, year FROM movies;

-- Seleccionar registros con condición
SELECT id, title, director FROM movies WHERE id = 1;
```

## Busqueda con restricciones

- =, !=, <, >, <=, >=: Operadores de comparación para valores numéricos y de texto.

    ```sql
    SELECT * FROM movies WHERE year = 2000;
    ```

- **BETWEEN**: Filtrar por rango de valores.

    ```sql
    SELECT * FROM movies WHERE year BETWEEN 2000 AND 2010;
    ```

- **NOT BETWEEN: Filstrar por rango de valores excluyendo los valores del rango.

    ```sql
    SELECT * FROM movies WHERE year NOT BETWEEN 2000 AND 2010;
    ```
- **IN**: Filtrar por lista de valores.

    ```sql
    SELECT * FROM movies WHERE year IN (2000, 2005, 2010);
    ```

- **NOT IN**: Filtrar excluyendo una lista de valores.

    ```sql
    SELECT * FROM movies WHERE year NOT IN (2000, 2005, 2010);
    ```

- **LIKE**: Filtrar por un patrón.

    ```sql
    SELECT * FROM movies WHERE title LIKE 'Toy%';
    ```

- **NOT LIKE**: Filtrar excluyendo un patrón.


    ```sql
    SELECT * FROM movies WHERE title NOT LIKE 'Toy%';
    ```

- **%**: Cualquier cadena de caracteres.

- **_**: Un solo caracter.

## Ordenar resultados

- **ORDER BY**: Ordenar resultados

    ```sql
    SELECT * FROM movies ORDER BY id DESC;
    ```

- **ASC**: Ordenar de forma ascendente
- **DESC**: Ordenar de forma descendiente

## Limitar resultados

- **LIMIT**: Limitar cantidad de registros

    ```sql
    SELECT * FROM movies LIMIT 5;
    ```

- **OFFSET**: Saltar la cantidad de registros

    ```sql
    SELECT * FROM movies LIMIT 5 OFFSET 5;
    ```

