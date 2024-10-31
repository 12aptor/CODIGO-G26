import express from "express";
import dotenv from "dotenv";
import { registerRoutes } from "./utils/lib";
import morgan from "morgan";

dotenv.config();

const app = express();
const PORT = process.env.PORT || 8080;

app.use(express.json());
app.use(morgan("dev"));

registerRoutes(app);

app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
