import { Router } from "express";
import * as userController from "../controllers/user.controller";

export const userRouter = Router();

userRouter
  .post("/create", userController.createUser)
  .get("/list", userController.listUsers);
