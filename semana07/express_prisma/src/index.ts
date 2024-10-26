import express from "express";
import { userRouter } from "./routes/user.router";

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.use("/api/user", userRouter);

app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
