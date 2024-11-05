import { Request, Response } from "express";
import { ZodError } from "zod";
import { prisma } from "../config/prisma";
import { message } from "../utils/constants";
import { ChannelSchema } from "../schemas/channel.schema";
import { getDownloadURL } from "firebase/storage";
import { userRef } from "../config/firebase";

export const createChannel = async (req: Request, res: Response) => {
  try {
    const validatedBody = ChannelSchema.parse(req.body);

    const channel = await prisma.channels.create({
      data: validatedBody,
    });

    res.status(201).json({
      message: "Canal creado exitosamente",
      data: channel,
    });
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
      });
      return;
    }
  }
};

export const getChannels = async (_req: Request, res: Response) => {
  try {
    const channels = await prisma.channels.findMany({
      orderBy: {
        id: "asc",
      },
    });

    res.status(200).json({
      message: "Canales obtenidos exitosamente",
      data: channels,
    });
    return;
  } catch (error) {
    if (error instanceof Error) {
      res.status(500).json({
        message: message.HTTP_500,
      });
      return;
    }
  }
};

export const getChannelMessages = async (req: Request, res: Response) => {
  try {
    const channelId = req.params.channelId;

    const messages = await prisma.messages.findMany({
      where: {
        channel_id: channelId,
      },
      orderBy: {
        created_at: "asc",
      },
      select: {
        id: true,
        content: true,
        created_at: true,
        author: {
          select: {
            id: true,
            username: true,
            avatar: true,
          },
        },
      },
    });

    let newMessages = [];

    for (let i = 0; i < messages.length; i++) {
      const message = messages[i];
      const avatarRef = userRef(message.author.avatar);
      const avatarUrl = await getDownloadURL(avatarRef);

      newMessages.push({
        ...message,
        author: {
          ...message.author,
          avatar: avatarUrl,
        },
      });
    }

    res.status(200).json({
      message: "Mensajes obtenidos exitosamente",
      data: newMessages,
    });
    return;
  } catch (error) {
    if (error instanceof Error) {
      res.status(500).json({
        message: message.HTTP_500,
        errors: error.message,
      });
      return;
    }
  }
};
