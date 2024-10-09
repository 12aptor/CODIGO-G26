import { API_URL } from "../lib/constants";

export const getUsersService = async () => {
  try {
    const response = await fetch(`${API_URL}/user/list`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });

    if (!response.ok) {
      return null;
    }

    const json = await response.json();
    return json;
  } catch {
    return null;
  }
};
