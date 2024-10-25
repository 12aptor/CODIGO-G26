"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const morgan_1 = __importDefault(require("morgan"));
const fs_1 = __importDefault(require("fs"));
const app = (0, express_1.default)();
const PORT = process.env.PORT || 3000;
const logStream = fs_1.default.createWriteStream("logs.txt", { flags: "a" });
app.use((0, morgan_1.default)("combined", { stream: logStream }));
app.use((0, morgan_1.default)("dev"));
const middleware = (req, res, next) => {
    const headers = req.headers;
    console.log(headers);
    console.log(res);
    next();
};
const home = (_req, res) => {
    res.send("Hello World!");
};
app.get("/", middleware, home);
app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
