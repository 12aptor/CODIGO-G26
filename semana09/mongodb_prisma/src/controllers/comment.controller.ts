import { Request, Response } from "express";
import { ZodError } from "zod";
import { CommentSchema } from "../schemas/comment.schema";
import { prisma } from "../config/prisma";

export const createComment = async (req: Request, res: Response) => {
  try {
    const validatedBody = CommentSchema.parse(req.body);

    const comment = await prisma.comments.create({
      data: validatedBody,
    });

    res.status(201).json({
      message: "Comentario creado exitosamente",
      data: comment,
    });
    return;
  } catch (error) {
    if (error instanceof ZodError) {
      res.status(400).json({
        message: "Error de validación",
        error: error.issues,
      });
      return;
    }

    if (error instanceof Error) {
      res.status(500).json({
        message: "Error inesperado, intente más tarde",
        error: error.message,
      });
      return;
    }
  }
};
