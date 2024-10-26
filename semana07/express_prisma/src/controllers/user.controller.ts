import { Request, Response } from "express";
import { UserSchema } from "../schemas/user.schema";
import { prisma } from "../config/prisma";
import { ZodError } from "zod";
import { messages } from "../utils/constants";

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
        message: messages.HTTP_400,
        errors: error.errors,
      });
    }

    if (error instanceof Error) {
      return res.status(500).json({
        message: messages.HTTP_500,
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
        message: messages.HTTP_500,
        errors: error.message,
      });
    }
  }
};

export const getUserById = async (req: Request, res: Response) => {
  try {
    const userId = parseInt(req.params.userId);

    const user = await prisma.users.findUnique({
      where: {
        id: userId,
      },
    });

    if (!user) {
      return res.status(404).json({
        message: "Usuario no encontrado",
      });
    }

    return res.status(200).json({
      message: "Usuario encontrado",
      data: user,
    });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(500).json({
        message: messages.HTTP_500,
        errors: error.message,
      });
    }
  }
};

export const updateUser = async (req: Request, res: Response) => {
  try {
    const userId = parseInt(req.params.userId);
    const validatedBody = UserSchema.parse(req.body);

    const user = await prisma.users.findUnique({
      where: {
        id: userId,
      },
    });

    if (!user) {
      return res.status(404).json({
        message: "Usuario no encontrado",
      });
    }

    const updatedUser = await prisma.users.update({
      where: {
        id: userId,
      },
      data: validatedBody,
    });

    return res.status(200).json({
      message: "Usuario actualizado exitosamente",
      data: updatedUser,
    });
  } catch (error) {
    if (error instanceof ZodError) {
      return res.status(400).json({
        message: messages.HTTP_400,
        errors: error.errors,
      });
    }

    if (error instanceof Error) {
      return res.status(500).json({
        message: messages.HTTP_500,
        errors: error.message,
      });
    }
  }
};

export const deleteUser = async (req: Request, res: Response) => {
  try {
    const userId = parseInt(req.params.userId);

    const user = await prisma.users.findUnique({
      where: {
        id: userId,
      },
    });

    if (!user) {
      return res.status(404).json({
        message: "Usuario no encontrado",
      });
    }

    await prisma.users.delete({
      where: {
        id: userId,
      },
    });

    return res.status(200).json({
      message: "Usuario eliminado exitosamente",
    });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(500).json({
        message: messages.HTTP_500,
      });
    }
  }
};
