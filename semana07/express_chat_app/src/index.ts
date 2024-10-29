import express from "express";
import dotenv from "dotenv";
import multer from "multer";

dotenv.config();

const app = express();
const PORT = process.env.PORT || 8080;

app.use(express.json());

const storage = multer.memoryStorage();
const upload = multer({ storage });

app.post("/", upload.single("avatar"), (req, res) => {
  console.log(req.body);
  console.log(req.file);
  res.send("Hello World!");
});

app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
