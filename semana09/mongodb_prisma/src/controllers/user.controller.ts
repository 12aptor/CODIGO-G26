import { Request, Response } from "express";
import { prisma } from "../config/prisma";
import { UserSchema } from "../schemas/user.schema";
import { ZodError } from "zod";

export const createUser = async (req: Request, res: Response) => {
  try {
    const validatedBody = UserSchema.parse(req.body);

    const user = await prisma.users.create({
      data: validatedBody,
    });

    res.status(201).json({
      message: "Usuario creado exitosamente",
      data: user,
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
