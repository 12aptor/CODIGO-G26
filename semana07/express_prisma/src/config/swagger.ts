import swaggerJSDoc from "swagger-jsdoc";

const swaggerDefinition = {
  openapi: "3.0.0",
  info: {
    title: "Express API",
    version: "0.0.1",
    description: "API para gestionar usuarios",
  },
  servers: [
    {
      url: "http://localhost:3000",
      description: "Localhost",
    },
  ],
  components: {
    schemas: {
      User: {
        type: "object",
        required: ["name", "email", "password"],
        properties: {
          id: {
            type: "integer",
            description: "ID del usuario",
            example: 1,
            format: "int64",
            readOnly: true,
          },
          name: {
            type: "string",
            description: "Nombre del usuario",
            example: "John Doe",
          },
          email: {
            type: "string",
            description: "Email del usuario",
            example: "john@example.com",
          },
          password: {
            type: "string",
            description: "Contraseña del usuario",
            example: "123456",
          }
        },
      },
      UserListResponse: {
        type: "object",
        properties: {
          message: {
            type: "string",
            description: "Lista de usuarios",
            example: "Lista de usuarios",
          },
          data: {
            type: "array",
            items: {
              $ref: "#/components/schemas/User",
            }
          }
        }
      },
      CreateUserResponse: {
        type: "object",
        properties: {
          message: {
            type: "string",
            description: "Usuario creado exitosamente",
            example: "Usuario creado exitosamente",
          },
          data: {
            $ref: "#/components/schemas/User"
          }
        }
      }
    },
  },
};

const options = {
  swaggerDefinition,
  apis: ["./src/routes/*.ts"],
};

export const swaggerSpec = swaggerJSDoc(options);
