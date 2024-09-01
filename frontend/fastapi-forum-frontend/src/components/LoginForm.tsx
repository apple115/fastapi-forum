import { useState } from "react";
import { Button } from "@/components/ui/button";
import Link from "next/link";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

const DOMAIN = "http://127.0.0.1:8000";
//TODO nextauth

const LoginForm: React.FC<{ onClose: () => void }> = ({ onClose }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch(`${DOMAIN}/api/v1/login/access-token`, {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
          grant_type: "password",
          username: username,
          password: password,
        }),
      });
      if (response.status === 200) {
        // 登录成功的处理逻辑
        console.log("登录成功");
        onClose();
      } else if (response.status === 401) {
        // 登录失败的处理逻辑
        console.error("用户名或密码错误");
      } else {
        console.error("未知错误");
      }
    } catch (error) {
      console.error("网络错误或其他异常", error);
    }
    //   onLogin(username, password, verificationCode);
  };

  return (
    <Card className=" fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-50 mx-auto max-w-sm ">
      <span
        className="absolute top-4 right-4 cursor-pointer text-2xl "
        onClick={onClose}
      >
        ×
      </span>
      <CardHeader>
        <CardTitle className="text-2xl">Login</CardTitle>
        <CardDescription>
          Enter your email below to login to your account
        </CardDescription>
      </CardHeader>
      <CardContent>
        <div className="grid gap-4">
          <div className="grid gap-2">
            <Label htmlFor="email">Email</Label>
            <Input
              id="email"
              type="email"
              placeholder="m@example.com"
              required
            />
          </div>
          <div className="grid gap-2">
            <div className="flex items-center">
              <Label htmlFor="password">Password</Label>
              <Link href="#" className="ml-auto inline-block text-sm underline">
                Forgot your password?
              </Link>
            </div>
            <Input id="password" type="password" required />
          </div>
          <Button type="submit" className="w-full">
            Login
          </Button>
        </div>
      </CardContent>
    </Card>
  );
};

export default LoginForm;
