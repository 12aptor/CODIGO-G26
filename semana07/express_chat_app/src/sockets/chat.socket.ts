import type { Server } from "socket.io";
import { IMessage } from "../types";
import { prisma } from "../config/prisma";
import { userRef } from "../config/firebase";
import { getDownloadURL } from "firebase/storage";
import { MessageSchema } from "../schemas/message.schema";

export const chatSocket = (io: Server) => {
  io.on("connection", (socket) => {
    socket.on("join", (channelId: string) => {
      socket.join(channelId);
    });

    socket.on("message", async (message: IMessage) => {
      try {
        const validatedMessage = MessageSchema.parse(message);

        const newMessage = await prisma.messages.create({
          data: validatedMessage,
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

        const avatarRef = userRef(newMessage.author.avatar);

        io.to(message.channel_id).emit("message", {
          ...newMessage,
          author: {
            ...newMessage.author,
            avatar: await getDownloadURL(avatarRef),
          },
        });
      } catch (error) {
        if (error instanceof Error) {
          socket.emit("error", {
            message: "Ocurrio un error al enviar el mensaje",
          });
        }
      }
    });

    socket.on("disconnect", () => {
      console.log("Cliente desconectado");
    });
  });
};
