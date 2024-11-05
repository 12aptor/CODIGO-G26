import express from "express";
import dotenv from "dotenv";
import { registerRoutes } from "./utils/lib";
import morgan from "morgan";
import swaggerUi from "swagger-ui-express";
import { swaggerSpec } from "./config/swagger";
import http from "http";
import { Server } from "socket.io";

dotenv.config();

const app = express();
const PORT = process.env.PORT || 8080;

const server = http.createServer(app);
const io = new Server(server, {
  cors: {
    origin: "*",
  },
});

app.use(express.json());
app.use(morgan("dev"));
app.use("/swagger", swaggerUi.serve, swaggerUi.setup(swaggerSpec));

registerRoutes(app);

io.on("connection", (socket) => {
  socket.on("message", (message) => {
    console.log("Mensaje recibido: ", message);
    io.emit("message", message);
  });

  socket.on("disconnect", () => {
    console.log("Cliente desconectado");
  });
});

server.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
