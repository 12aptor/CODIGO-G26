import express from "express";
import dotenv from "dotenv";
import { registerRoutes } from "./utils/lib";

dotenv.config();

const app = express();
const PORT = process.env.PORT || 8080;

app.use(express.json());

registerRoutes(app);

app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
