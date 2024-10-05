import { API_URL } from "../lib/constants";

export const loginService = async (credentials: any) => {
  const response = await fetch(`${API_URL}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(credentials),
  });

  const status = response.status;
  const json = await response.json();

  return { status, json };
};
