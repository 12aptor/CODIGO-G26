import { Request, Response, NextFunction } from "express";
import { message } from "../utils/constants";
import jwt, { JsonWebTokenError } from "jsonwebtoken";

export const authMiddleware = (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const token = req.headers.authorization;

    if (!token) {
      res.status(401).json({
        message: message.HTTP_401,
      });
      return;
    }

    const secret = process.env.SECRET_KEY;

    if (!secret) {
      throw new Error("No se ha configurado el SECRET_KEY");
    }

    const jwtToken = token.split(" ")[1];
    const decodedToken = jwt.verify(jwtToken, secret);

    if (!decodedToken) {
      res.status(401).json({
        message: message.HTTP_401,
      });
      return;
    }

    next();
  } catch (error) {
    if (error instanceof JsonWebTokenError) {
      res.status(401).json({
        message: message.HTTP_401,
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
