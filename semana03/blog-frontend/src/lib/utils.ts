import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export const cn = (...inputs: ClassValue[]) => {
  return twMerge(clsx(inputs));
};

export const isAuthenticated = (): boolean => {
  try {
    const jwt = localStorage.getItem("token");

    if (!jwt) {
      return false;
    }

    const payload = jwt.split(".")[1];
    const decoded = atob(payload);
    const json = JSON.parse(decoded);

    if (json.exp < Date.now() / 1000) {
      return false;
    }

    return true;
  } catch {
    return false;
  }
};
