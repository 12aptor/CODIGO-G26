import multer from "multer";
import { type Application } from "express";
import fs from "fs";
import path from "path";
import { authMiddleware } from "../config/middleware";

const storage = multer.memoryStorage();
export const upload = multer({ storage });

export const registerRoutes = (app: Application) => {
  const routesPath = path.join(__dirname, "..", "routes");

  fs.readdirSync(routesPath).forEach(async (file) => {
    if (file.endsWith(".router.ts")) {
      const { router } = await import(path.join(routesPath, file));
      const modulePath = file.split(".router.ts")[0];
      const routePath = `/api/${modulePath}`;
      if (modulePath === "auth") {
        app.use(routePath, router);
      } else {
        app.use(routePath, authMiddleware, router);
      }
    }
  });
};
