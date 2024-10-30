import { Request, Response } from "express";
import { LoginSchema, RegisterSchema } from "../schemas/auth.schema";
import { ZodError } from "zod";
import { message } from "../utils/constants";
import { getDownloadURL, uploadBytes } from "firebase/storage";
import { prisma } from "../config/prisma";
import bcrypt from "bcrypt";
import { nanoid } from "nanoid";
import { userRef } from "../config/firebase";
import jwt from "jsonwebtoken";

export const register = async (req: Request, res: Response) => {
  try {
    const avatar = req.file;

    if (!avatar) {
      throw new ZodError([
        {
          code: "invalid_type",
          expected: "object",
          received: "undefined",
          path: ["avatar"],
          message: "Avatar is required",
        },
      ]);
    }

    const validatedBody = RegisterSchema.parse(req.body);

    const avatarKey = `${nanoid(5)}-${avatar.originalname}`;
    const avatarRef = userRef(avatarKey);
    const firebaseResponse = await uploadBytes(avatarRef, avatar.buffer);

    if (!firebaseResponse.metadata) {
      throw new Error("Error al subir el avatar");
    }

    const user = await prisma.users.create({
      data: {
        ...validatedBody,
        avatar: avatarKey,
        password: await bcrypt.hash(validatedBody.password, 10),
      },
      select: {
        id: true,
        username: true,
        email: true,
        avatar: true,
        status: true,
      },
    });

    res.status(201).json({
      message: "Usuario creado exitosamente",
      data: {
        ...user,
        avatar: await getDownloadURL(avatarRef),
      },
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

export const login = async (req: Request, res: Response) => {
  try {
    const validatedBody = LoginSchema.parse(req.body);

    const user = await prisma.users.findUnique({
      where: {
        email: validatedBody.email,
      },
    });

    if (!user) {
      res.status(401).json({
        message: message.HTTP_401,
      });
      return;
    }

    const isPasswordCorrect = await bcrypt.compare(
      validatedBody.password,
      user.password
    );

    if (!isPasswordCorrect) {
      res.status(401).json({
        message: message.HTTP_401,
      });
      return;
    }

    const secret = process.env.SECRET_KEY;

    if (!secret) {
      throw new Error("No se ha configurado el SECRET_KEY");
    }

    const accessToken = jwt.sign(
      {
        id: user.id,
        username: user.username,
        email: user.email,
        avatar: user.avatar,
      },
      secret,
      {
        expiresIn: "7d",
      }
    );

    res.status(200).json({
      message: "Sesión iniciada exitosamente",
      data: {
        access: accessToken,
      },
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
