import { Router } from "express";
import * as authController from "../controllers/auth.controller";
import { upload } from "../utils/lib";

export const router = Router();

/**
 * @swagger
 * /api/auth/register:
 *   post:
 *     summary: Ruta para registrar un usuario
 *     description: Registrar un usuario
 *     tags: [Autenticacion]
 *     requestBody:
 *       required: true
 *       content:
 *         multipart/form-data:
 *           schema:
 *             $ref: '#/components/schemas/Register'
 *     responses:
 *       201:
 *         description: Usuario creado exitosamente
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/RegisterResponse'
 */
router.post("/register", upload.single("avatar"), authController.register);

/**
 * @swagger
 * /api/auth/login:
 *   post:
 *     summary: Ruta para iniciar sesión
 *     description: Iniciar sesión
 *     tags: [Autenticacion]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             $ref: '#/components/schemas/Login'
 *     responses:
 *       200:
 *         description: Sesión iniciada exitosamente
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/LoginResponse'
 */
router.post("/login", authController.login);
