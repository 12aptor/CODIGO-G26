import { useEffect, useState } from "react";
import { getPostsService } from "../../services/post_service";
import { IPost } from "../../types";

export const Posts = () => {
  const [posts, setPosts] = useState<IPost[]>([]);

  useEffect(() => {
    getPostsService().then((response) => {
      if (response) {
        setPosts(response.data);
      }
    });
  }, []);

  return (
    <div className="w-4/5 max-w-[1200px] mx-auto p-5">
      <h1 className="text-center text-gray-800">Novedades de programación</h1>
      <div className="flex flex-wrap">
        {posts.map((post) => (
          <div
            key={post.id}
            className="w-[calc(100%/3)] p-4 border border-gray-300 rounded-lg"
          >
            <picture className="rounded-md overflow-hidden">
              <img src={post.image} alt="Imagen de la novedad" />
            </picture>
            <h2 className="text-xl font-bold">{post.title}</h2>
            <div className="flex justify-between gap-5">
              <span className="text-ellipsis text-xs whitespace-nowrap">
                {post.author.name}
              </span>
              <span className="text-xs whitespace-nowrap">
                {post.created_at}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
