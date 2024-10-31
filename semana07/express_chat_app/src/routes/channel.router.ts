import { Router } from "express";
import * as channelController from "../controllers/channel.controller";

export const router = Router();

/**
 * @swagger
 * /api/channel/create:
 *   post:
 *     summary: Ruta para crear un canal
 *     description: Crear un canal
 *     tags: [Canal]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             $ref: '#/components/schemas/Channel'
 *     responses:
 *       201:
 *         description: Canal creado exitosamente
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/CreateChannelResponse'
 */
router.post("/create", channelController.createChannel);
router.get("/list", channelController.getChannels);
