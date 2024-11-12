import express from "express";
import { userRouter } from "./router/user.router";
import { postRouter } from "./router/post.router";
import { commentRouter } from "./router/comment.router";

const app = express();
const PORT = process.env.PORT || 8080;

app.use(express.json());

app.use("/api/user", userRouter);
app.use("/api/post", postRouter);
app.use("/api/comment", commentRouter);

app.listen(PORT, () => {
  console.log(`Running app: http://localhost:${PORT}`);
});
