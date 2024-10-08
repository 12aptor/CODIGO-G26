import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getPostService } from "../../services/post_service";
import { IPost } from "../../types";

export const Post = () => {
  const { postId } = useParams();
  const [post, setPost] = useState<IPost | null>(null);

  useEffect(() => {
    if (!postId) return;

    getPostService(postId).then((response) => {
      if (response) {
        setPost(response.data);
      }
    });
  }, [postId]);

  return (
    <div className="w-4/5 max-w-[1200px] mx-auto p-5">
      <h1>{post?.title}</h1>
      <p>{post?.content}</p>
    </div>
  );
};
