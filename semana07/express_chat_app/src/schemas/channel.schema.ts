import { z } from "zod";

export const ChannelSchema = z.object({
  name: z.string().min(3).max(20).trim(),
  type: z.enum(["TEXT", "VOICE"]).default("TEXT"),
});
