# MongoDB

## Instalación

- Instalar MongoDB Server
- Instalar MongoDB Compass
- Instalar MongoDB Shell

## Abrir MongoDB Shell

```bash
mongosh
```

## Mostrar las bases de datos

```bash
show dbs
```

## Conectar o crear una base de datos

```bash
use <nombre-base-de-datos>
```

## Eliminar una base de datos

```javascript
db.dropDatabase()
```

## Crear una colección

```javascript
db.createCollection("nombre-coleccion")
// ó
db.customers.insertOne({ name: "John Doe", age: 20 })
```

## Mostrar las colecciones

```bash
show collections
```

## Eliminar una colección

```javascript
db.customers.drop()
```

## Insertar datos en una colección

```javascript
db.customers.insertOne({ name: "John Doe", age: 20 })

db.customers.insertMany([
    { name: "John Doe", age: 20 },
    { name: "Bob Smith", age: 25 },
    { name: "Alice Johnson", age: 30 }
])

db.customers.insertOne({
    name: "Charlie Brown",
    age: 40,
    tags: ["cool", "funny"],
    address: {
        street: "123 Main St",
        city: "Anytown",
        state: "CA",
        coordinates: [-122.42283, 37.77717]
    }
})
```

## Buscar datos en una colección

```javascript
db.customers.find()
db.customers.find({ name: "John Doe" })
db.customers.find({ age: 30 })
db.customers.findOne({ age: 30 })
```

## Actualizar datos en una colección

```javascript
db.customers.updateOne(
    { name: "John Doe" },
    { $set: { age: 25 }}
)
```

## Eliminar datos de una colección

```javascript
db.customers.deleteOne({ name: "John Doe" })
```

## Eliminar la propiedad de un documento

```javascript
db.customers.updateOne(
    { _id: ObjectId('672eade40800e6a0600d8194') },
    { $unset: { tags: 1 }}
)
```

## Ordenar datos de una colección

```javascript
db.customers.find().sort({ age: 1 })
```

## Limitar los resultados de una colección

```javascript
db.customers.find().limit(2);
```

## Paginación

```javascript
db.customers.find().skip(1).limit(1).sort({ age: 1 })
```

## Buscadas avanzadas

### Operadores de comparación
- $eq: Igual a
    ```javascript
    db.customers.find({
        age: {
            $eq: 30
        }
    })
    ```

- $ne: No igual a
    ```javascript
    db.customers.find({
        age: {
            $ne: 30
        }
    })
    ```

- $gt: Mayor que
    ```javascript
    db.customers.find({
        age: {
            $gt: 30
        }
    })
    ```

- $gte: Mayor o igual que
    ```javascript
    db.customers.find({
        age: {
            $gte: 30
        }
    })
    ```

- $lt: Menor que
    ```javascript
    db.customers.find({
        age: {
            $lt: 30
        }
    })
    ```

- $lte: Menor o igual que
    ```javascript
    db.customers.find({
        age: {
            $lte: 30
        }
    })
    ```

- $in: Incluye
    ```javascript
    db.customers.find({
        tags: {
            $in: ["cool"]
        }
    })
    ```

- $nin: No incluye
    ```javascript
    db.customers.find({
        tags: {
            $nin: ["cool"]
        }
    })
    ```

### Operadores lógicos

- $and: Combina condiciones, todos deben cumplirse
    ```javascript
    db.customers.find({
        $and: [
            {
                age: {
                    $gt: 30
                }
            },
            {
                tags: {
                    $in: ["cool"]
                }
            }
        ]
    })
    ```

- $or: Combina condiciones, al menos una debe cumplirse
    ```javascript
    db.customers.find({
        $or: [
            {
                age: {
                    $gt: 30
                }
            },
            {
                tags: {
                    $in: ["cool"]
                }
            }
        ]
    })
    ```

- $not: Inversa la condición
    ```javascript
    db.customers.find({
        age: {
            $not: {
                $gt: 30
            }
        }
    })
    ```

- $nor: Inversa la condición combinada con $or
    ```javascript
    db.customers.find({
        $nor: [
            {
                age: {
                    $gt: 30
                }
            },
            {
                tags: {
                    $in: ["cool"]
                }
            }
        ]
    })
    ```

### Operadores de elementos

- $exists: Verifica si existe un campo
    ```javascript
    db.customers.find({
        tags: {
            $exists: true
        }
    })
    ```

- $type: Verifica el tipo de un campo
    ```javascript
    db.customers.find({
        age: {
            $type: "number"
        }
    })
    ```

- $regex: Verifica si el campo coincide con una expresión regular
    ```javascript
    db. customers.find({
        name: {
            $regex: /^J/
        }
    })
    ```

### Consultas en arrays

- $elemMatch: Verifica si un campo es igual a un valor
    ```javascript
    db.customers.find({
        tags: {
            $elemMatch: {
                $eq: "cool"
            }
        }
    })
    ```

- $size: Verifica el tamaño de un array
    ```javascript
    db.customers.find({
        'address.coordinates': {
            $size: 2
        }
    })
    ```