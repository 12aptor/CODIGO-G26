import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Login } from "./components/pages/login";
import { Toaster } from "react-hot-toast";
import { Register } from "./components/pages/register";
import { Posts } from "./components/pages/posts";
import "./index.css";

const router = createBrowserRouter([
  {
    path: "",
    element: <Posts />,
    errorElement: <div>Error</div>,
  },
  {
    path: "/post/:id",
    element: <div>Post</div>,
  },
  {
    path: "/registro",
    element: <Register />,
  },
  {
    path: "/login",
    element: <Login />,
  },
]);

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <RouterProvider router={router} />
    <Toaster position="top-center" />
  </StrictMode>
);
