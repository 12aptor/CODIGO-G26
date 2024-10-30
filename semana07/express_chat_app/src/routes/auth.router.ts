import { Router } from "express";
import * as authController from "../controllers/auth.controller";
import { upload } from "../utils/lib";

export const router = Router();

router.post("/register", upload.single("avatar"), authController.register);
router.post("/login", authController.login);
