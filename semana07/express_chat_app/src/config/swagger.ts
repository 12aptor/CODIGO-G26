import swaggerJSDoc from "swagger-jsdoc";

const swaggerDefinition = {
  openapi: "3.0.0",
  info: {
    title: "Express Chat App",
    version: "0.0.1",
    description: "API para una aplicación de chat en tiempo real",
  },
  servers: [
    {
      url: "http://localhost:8080",
      description: "Localhost",
    },
  ],
  components: {
    schemas: {
      Channel: {
        type: "object",
        properties: {
          id: {
            type: "string",
            format: "uuid",
            description: "ID del canal",
            example: "123e4567-e89b-12d3-a456-426614174000",
            readOnly: true,
          },
          name: {
            type: "string",
            description: "Nombre del canal",
            example: "Canal de prueba",
          },
          type: {
            type: "string",
            description: "Tipo de canal",
            example: "TEXT",
            enum: ["TEXT", "VOICE"],
          },
          created_at: {
            type: "string",
            format: "date-time",
            description: "Fecha de creación del canal",
            example: "2023-05-01T00:00:00.000Z",
            readOnly: true,
          },
          updated_at: {
            type: "string",
            format: "date-time",
            description: "Fecha de actualización del canal",
            example: "2023-05-01T00:00:00.000Z",
            readOnly: true,
          },
        },
      },
      CreateChannelResponse: {
        type: "object",
        properties: {
          message: {
            type: "string",
            description: "Mensaje de respuesta",
            example: "Canal creado exitosamente",
          },
          data: {
            $ref: "#/components/schemas/Channel",
          },
        },
      },
      ListChannelResponse: {
        type: "object",
        properties: {
          message: {
            type: "string",
            description: "Mensaje de respuesta",
            example: "Canales obtenidos exitosamente",
          },
          data: {
            type: "array",
            items: {
              $ref: "#/components/schemas/Channel",
            },
          },
        },
      },
      Login: {
        type: "object",
        properties: {
          email: {
            type: "string",
            description: "Correo electrónico del usuario",
            example: "usuario@ejemplo.com",
          },
          password: {
            type: "string",
            description: "Contaseña del usuario",
            example: "123456",
          },
        },
      },
      LoginResponse: {
        type: "object",
        properties: {
          message: {
            type: "string",
            description: "Mensaje de respuesta",
            example: "Sesión iniciada exitosamente",
          },
          data: {
            type: "object",
            properties: {
              access: {
                type: "string",
                description: "Token de acceso",
                example:
                  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
              },
            },
          },
        },
      },
      Register: {
        type: "object",
        required: ["username", "email", "password", "avatar"],
        properties: {
          username: {
            type: "string",
            description: "Nombre de usuario",
            example: "usuario",
          },
          email: {
            type: "string",
            description: "Correo electrónico del usuario",
            example: "usuario@ejemplo.com",
            format: "email",
          },
          password: {
            type: "string",
            description: "Contraseña del usuario",
            example: "123456",
          },
          avatar: {
            type: "string",
            description: "Imagen del usuario",
            format: "binary",
          },
          status: {
            type: "string",
            description: "Estado del usuario",
            example: "ONLINE",
            enum: ["ONLINE", "OFFLINE", "IDLE"],
            readOnly: true,
          },
        },
      },
      ListChannelMessagesResponse: {
        type: "object",
        properties: {
          message: {
            type: "string",
            description: "Mensaje de respuesta",
            example: "Mensajes obtenidos exitosamente",
          },
          data: {
            type: "array",
            items: {
              type: "object",
              properties: {
                id: {
                  type: "number",
                  description: "ID del mensaje",
                  example: 1,
                },
                content: {
                  type: "string",
                  description: "Contenido del mensaje",
                  example: "Hola, ¿Cómo estás?",
                },
                created_at: {
                  type: "string",
                  format: "date-time",
                  description: "Fecha de creación del mensaje",
                  example: "2023-05-01T00:00:00.000Z",
                },
                author: {
                  type: "object",
                  properties: {
                    id: {
                      type: "number",
                      description: "ID del autor del mensaje",
                      example: 1,
                    },
                    username: {
                      type: "string",
                      description: "Nombre del autor del mensaje",
                      example: "usuario",
                    },
                    avatar: {
                      type: "string",
                      description: "URL de la imagen del autor del mensaje",
                      example: "https://example.com/avatar.png",
                    },
                  },
                },
              },
            },
          },
        },
      },
    },
  },
};

const options = {
  swaggerDefinition: swaggerDefinition,
  apis: ["./src/routes/*.ts"],
};

export const swaggerSpec = swaggerJSDoc(options);
