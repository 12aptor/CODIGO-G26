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

/**
 * @swagger
 * /api/channel/list:
 *   get:
 *     summary: Ruta para obtener los canales
 *     description: Obtener los canales
 *     tags: [Canal]
 *     responses:
 *       200:
 *         description: Canales obtenido exitosamente
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/ListChannelResponse'
 */
router.get("/list", channelController.getChannels);

/**
 * @swagger
 * /api/channel/messages/{channelId}:
 *   get:
 *     summary: Ruta para obtener los mensajes de un canal
 *     description: Obtener los mensajes de un canal
 *     tags: [Canal]
 *     parameters:
 *       - in: path
 *         name: channelId
 *         required: true
 *     responses:
 *       200:
 *         description: Mensajes obtenidos exitosamente
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/ListChannelMessagesResponse'
 */
router.get("/messages/:channelId", channelController.getChannelMessages);