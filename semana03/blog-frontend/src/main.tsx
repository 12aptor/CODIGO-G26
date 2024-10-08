import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Login } from "./components/pages/login";
import { Toaster } from "react-hot-toast";
import { Register } from "./components/pages/register";
import { Posts } from "./components/pages/posts";
import { Post } from "./components/pages/post";
import "./index.css";
import { Backoffice } from "./components/pages/backoffice";

const router = createBrowserRouter([
  {
    path: "",
    element: <Posts />,
    errorElement: <div>Error</div>,
  },
  {
    path: "/post/:postId",
    element: <Post />,
  },
  {
    path: "/registro",
    element: <Register />,
  },
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/backoffice",
    element: <Backoffice />,
  },
]);

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <RouterProvider router={router} />
    <Toaster position="top-center" />
  </StrictMode>
);
