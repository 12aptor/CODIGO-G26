import { z } from "zod";

export const MessageSchema = z.object({
  content: z.string().min(1).max(1000).trim(),
  channel_id: z.string(),
  author_id: z.number(),
});
