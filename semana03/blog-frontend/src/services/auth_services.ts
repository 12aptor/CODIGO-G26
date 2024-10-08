import { API_URL } from "../lib/constants";
import { ICredentials, IRegisterUser } from "../types";

export const loginService = async (credentials: ICredentials) => {
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

export const registerService = async (userData: IRegisterUser) => {
  const response = await fetch(`${API_URL}/auth/register`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(userData),
  });

  const status = response.status;
  const json = await response.json();

  return { status, json };
};
