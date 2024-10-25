import express, { Request, Response } from "express";
import morgan from "morgan";
import fs from "fs";

const app = express();
const PORT = process.env.PORT || 3000;

const logStream = fs.createWriteStream("logs.txt", { flags: "a" });

app.use(morgan("combined", { stream: logStream }));
app.use(morgan("dev"));

const middleware = (req: Request, res: Response, next: () => void) => {
  const headers = req.headers;
  console.log(headers);
  console.log(res);
  next();
};

const home = (_req: Request, res: Response) => {
  res.send("Hello World!");
};

app.get("/", middleware, home);

app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
