import { API_URL } from "../lib/constants";

export const getPostsService = async () => {
  try {
    const response = await fetch(`${API_URL}/post/list`);

    if (!response.ok) {
      return null;
    }

    const json = await response.json();

    return json;
  } catch {
    return null;
  }
};

export const getPostService = async (postId: string) => {
  try {
    const response = await fetch(`${API_URL}/post/get/${postId}`);

    if (!response.ok) {
      return null;
    }

    const json = await response.json();

    return json;
  } catch {
    return null;
  }
};
