import { Request, Response } from "express";
import { UserSchema } from "../schemas/user.schema";
import { prisma } from "../config/prisma";
import { ZodError } from "zod";

export const createUser = async (req: Request, res: Response) => {
  try {
    const validatedBody = UserSchema.parse(req.body);

    const user = await prisma.users.create({
      data: validatedBody,
    });

    return res.status(200).json({
      message: "Usuario creado exitosamente",
      data: user,
    });
  } catch (error) {
    if (error instanceof ZodError) {
      return res.status(400).json({
        message: "Error al validar la información",
        errors: error.errors,
      });
    }

    if (error instanceof Error) {
      return res.status(500).json({
        message: "Ha ocurrido un error inesperado, intenta de nuevo",
        errors: error.message,
      });
    }
  }
};

export const listUsers = async (_req: Request, res: Response) => {
  try {
    const users = await prisma.users.findMany({
      orderBy: {
        id: "asc",
      },
    });

    return res.status(200).json({
      message: "Lista de usuarios",
      data: users,
    });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(500).json({
        message: "Ha ocurrido un error inesperado, intenta de nuevo",
        errors: error.message,
      });
    }
  }
};
