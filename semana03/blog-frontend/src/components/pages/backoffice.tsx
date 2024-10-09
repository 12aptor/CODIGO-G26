import { useEffect, useState } from "react";
import { isAuthenticated } from "../../lib/utils";
import { Navigate } from "react-router-dom";
import { getUsersService } from "../../services/user_services";

export const Backoffice = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    getUsersService().then((response) => {
      if (response) {
        setUsers(response.data);
      }
    });
  }, []);

  console.log(users);

  if (!isAuthenticated()) {
    return <Navigate to="/login" />;
  }

  return <div></div>;
};
