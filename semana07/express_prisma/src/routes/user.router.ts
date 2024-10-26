import { Router } from "express";
import * as userController from "../controllers/user.controller";

export const userRouter = Router();

userRouter
  /**
   * @swagger
   * /api/user/create:
   *   post:
   *     summary: Ruta para crear un usuario
   *     description: Crear un usuario
   *     tags: [Usuario]
   *     requestBody:
   *       required: true
   *       content:
   *         application/json:
   *           schema:
   *             $ref: '#/components/schemas/User'
   *     responses:
   *       201:
   *         description: Usuario creado exitosamente
   *         content:
   *           application/json:
   *             schema:
   *               $ref: '#/components/schemas/CreateUserResponse'
   */
  .post("/create", userController.createUser)
  /**
   * @swagger
   * /api/user/list:
   *   get:
   *     summary: Ruta para listar usuarios
   *     description: Listar usuarios
   *     tags: [Usuario]
   *     responses:
   *       200:
   *         description: Lista de usuarios
   *         content:
   *           application/json:
   *             schema:
   *               $ref: '#/components/schemas/UserListResponse'
   */
  .get("/list", userController.listUsers)
  .get("/by-id/:userId", userController.getUserById)
  .put("/update/:userId", userController.updateUser)
  .delete("/delete/:userId", userController.deleteUser);
