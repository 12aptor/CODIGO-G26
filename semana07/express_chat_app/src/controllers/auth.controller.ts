import { Request, Response } from "express";
import { RegisterSchema } from "../schemas/auth.schema";
import { ZodError } from "zod";
import { message } from "../utils/constants";
import { getStorage, ref, uploadBytes} from "firebase/storage";
import { firebaseApp } from "../config/firebase";

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

    const storage = getStorage(firebaseApp);
    const storageRef = ref(storage, `users/avatars/${avatar.originalname}`);
    const firebaseResponse = await uploadBytes(storageRef, avatar.buffer);

  } catch (error) {
    if (error instanceof ZodError) {
      return res.status(400).json({
        message: message.HTTP_400,
        errors: error.errors,
      });
    }

    if (error instanceof Error) {
      return res.status(500).json({
        message: message.HTTP_500,
        error: error.message,
      });
    }
  }
};

export const login = (req: Request, res: Response) => {
  try {
    // Manejo de la autenticación
  } catch (error) {
    // Manejo de errores
  }
};
