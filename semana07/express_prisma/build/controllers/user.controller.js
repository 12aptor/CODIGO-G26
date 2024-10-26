"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.createUser = void 0;
const user_schema_1 = require("../schemas/user.schema");
const prisma_1 = require("../config/prisma");
const zod_1 = require("zod");
const createUser = (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        const validatedBody = user_schema_1.UserSchema.parse(req.body);
        const user = yield prisma_1.prisma.users.create({
            data: validatedBody,
        });
        return res.status(200).json({
            message: "Usuario creado exitosamente",
            data: user,
        });
    }
    catch (error) {
        if (error instanceof zod_1.ZodError) {
            return res.status(400).json({
                message: "Error al validar la información",
                errors: error.errors,
            });
        }
        if (error instanceof Error) {
            return res.status(500).json({
                message: "Ha ocurrido un error inesperado, intenta de nuevo",
                errors: error.message,
            });
        }
    }
});
exports.createUser = createUser;
