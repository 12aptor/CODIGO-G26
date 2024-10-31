import express from "express";
import dotenv from "dotenv";
import { registerRoutes } from "./utils/lib";
import morgan from "morgan";
import swaggerUi from "swagger-ui-express";
import { swaggerSpec } from "./config/swagger";

dotenv.config();

const app = express();
const PORT = process.env.PORT || 8080;

app.use(express.json());
app.use(morgan("dev"));
app.use("/swagger", swaggerUi.serve, swaggerUi.setup(swaggerSpec));

registerRoutes(app);

app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
