import { Router } from "express";
import * as commentController from "../controllers/comment.controller";

export const commentRouter = Router();

commentRouter.post("/create", commentController.createComment);
