import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Login } from "./components/pages/login";
import "./index.css";

const router = createBrowserRouter([
  {
    path: "",
    element: <div>Home</div>,
  },
  {
    path: "/post/:id",
    element: <div>Post</div>,
  },
  {
    path: "/registro",
    element: <div>Registros</div>,
  },
  {
    path: "/login",
    element: <Login />
  },
]);

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);
