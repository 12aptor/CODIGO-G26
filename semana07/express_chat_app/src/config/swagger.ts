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
    },
  },
};

const options = {
  swaggerDefinition: swaggerDefinition,
  apis: ["./src/routes/*.ts"],
};

export const swaggerSpec = swaggerJSDoc(options);
