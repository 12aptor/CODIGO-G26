# Prisma ORM

## Instalación

```bash
npm install prisma -D
```

## Configuración

```bash
npx prisma init
# Si queremos usar otra base de datos
npx prisma init --datasource-provider postgresql
npx prisma init --datasource-provider mysql
npx prisma init --datasource-provider mongodb
npx prisma init --datasource-provider sqlserver
npx prisma init --datasource-provider sqlite
```

## Formatear el código

```bash
npx prisma format
```

## Crear migraciones

```bash
npx prisma migrate dev --name "nombre_migracion"
```

## Instalar Prisma client

```bash
npm install @prisma/client
```
