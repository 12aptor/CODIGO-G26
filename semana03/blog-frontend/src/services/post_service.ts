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
