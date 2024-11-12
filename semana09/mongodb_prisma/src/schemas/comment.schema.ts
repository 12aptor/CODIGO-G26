import { z } from "zod";

export const CommentSchema = z.object({
  content: z.string().min(1).max(1000),
  post_id: z.string(),
  author_id: z.string(),
});
