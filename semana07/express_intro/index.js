import express from "express";
import morgan from "morgan";
import fs from "fs";

const app = express();

const logStream = fs.createWriteStream("logs.txt", { flags: "a" });

app.use(morgan("combined", { stream: logStream }));
app.use(morgan("dev"));

// Para procesar json
app.use(express.json());

// Middleware global
app.use((req, res, next) => {
  const url = req.url;
  const method = req.method;
  const headers = req.headers;

  // Lógica para determinar si se debe continuar o no
  next();
});

// Middleware para rutas específicas
const middleware = (req, res, next) => {
  const url = req.url;
  const method = req.method;
  const headers = req.headers;

  // Lógica para determinar si se debe continuar o no
  next();
};

app.get("/", middleware, (req, res) => {
  res.send("Hola mundo!");
});

// Recuperar parametros de la URL
app.get("/user/:userId", (req, res) => {
  const userId = parseInt(req.params.userId);
  console.log(typeof userId);

  // Recuperar el método HTTP
  const method = req.method;
  console.log(method);

  // Recuperar la URL
  const url = req.url;
  const path = req.path;
  console.log(url);
  console.log(path);

  // Recuperar el body (El método GET no tiene body)
  const body = req.body;
  console.log(body);

  res.send(`User Id: ${userId}`);
});

app.listen(3000, () => {
  console.log("Servidor corriendo en http://localhost:3000");
});
