import { useState, ChangeEvent, FormEvent } from "react";
import { Card } from "../ui/card";
import { Input } from "../ui/input";
import { Label } from "../ui/label";
import { LockIcon, MailIcon } from "lucide-react";
import { Button } from "../ui/button";
import { loginService } from "../../services/auth_services";

export const Login = () => {
  const [credentials, setCredentials] = useState({
    email: "",
    password: "",
  });

  const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.currentTarget;

    setCredentials({
      ...credentials,
      [name]: value,
    });
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const { status, json } = await loginService(credentials);

      if (status === 200) {
        console.log(json);
      }

      throw new Error(json.message);
    } catch (error) {
      if (error instanceof Error) {
        console.log(error.message);
      }
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <Card className="w-full max-w-md mx-auto">
        <div className="flex flex-col space-y-1.5 p-6">
          <h1 className="text-2xl font-bold">Login</h1>
          <p className="text-sm text-gray-600">
            Ingresa tus credenciales para acceder a tu cuenta
          </p>
        </div>
        <div className="p-6 pt-0">
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="email">Correo</Label>
              <div className="relative">
                <MailIcon className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
                <Input
                  id="email"
                  type="email"
                  name="email"
                  placeholder="email@example.com"
                  className="pl-10"
                  onChange={handleInputChange}
                  required
                />
              </div>
            </div>
            <div className="space-y-2">
              <Label htmlFor="password">Contraseña</Label>
              <div className="relative">
                <LockIcon className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
                <Input
                  id="password"
                  type="password"
                  name="password"
                  placeholder="********"
                  className="pl-10"
                  onChange={handleInputChange}
                  required
                />
              </div>
            </div>
            <div className="flex items-center space-x-2">
              <input type="checkbox" id="remember" />
              <Label htmlFor="remember" className="text-sm font-normal">
                Recordarme
              </Label>
            </div>
            <Button className="w-full" type="submit">
              Login
            </Button>
          </form>
        </div>
      </Card>
    </div>
  );
};
