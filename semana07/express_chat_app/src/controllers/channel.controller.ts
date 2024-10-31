import { Request, Response } from "express";
import { ZodError } from "zod";
import { prisma } from "../config/prisma";
import { message } from "../utils/constants";
import { ChannelSchema } from "../schemas/channel.schema";

export const createChannel = async (req: Request, res: Response) => {
  try {
    const validatedBody = ChannelSchema.parse(req.body);

    const channel = await prisma.channels.create({
        data: validatedBody,
    })

    res.status(201).json({
        message: "Canal creado exitosamente",
        data: channel,
    })
    return;
  } catch (error) {
    if (error instanceof ZodError) {
      res.status(400).json({
        message: message.HTTP_400,
        errors: error.errors,
      });
      return;
    }

    if (error instanceof Error) {
        res.status(500).json({
            message: message.HTTP_500,
            errors: error.message,
        })
        return;
    }
  }
};
