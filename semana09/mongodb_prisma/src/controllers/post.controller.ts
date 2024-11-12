import { Request, Response } from "express";
import { prisma } from "../config/prisma";
import { PostSchema } from "../schemas/post.schema";
import { ZodError } from "zod";

export const createPost = async (req: Request, res: Response) => {
  try {
    const validatedBody = PostSchema.parse(req.body);

    const post = await prisma.posts.create({
      data: validatedBody,
    });

    res.status(201).json({
      message: "Post creado exitosamente",
      data: post,
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

export const getPosts = async (req: Request, res: Response) => {
  try {
    const queryParams = req.query;
    const page = parseInt(queryParams.page as string) - 1;
    const limit = parseInt(queryParams.limit as string);

    const posts = await prisma.posts.findMany({
      skip: page * limit,
      take: limit,
      include: {
        author: true,
        comments: {
          include: {
            author: true,
          },
        },
      },
    });

    res.status(200).json({
      message: "Posts obtenidos exitosamente",
      data: posts,
    });
    return;
  } catch (error) {
    if (error instanceof Error) {
      res.status(500).json({
        message: "Error inesperado, intente más tarde",
        error: error.message,
      });
      return;
    }
  }
};
