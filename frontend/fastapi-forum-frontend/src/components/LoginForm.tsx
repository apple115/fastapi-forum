import { useState } from "react";

const LoginForm: React.FC<{ onClose: () => void }> = ({ onClose }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [verificationCode, setVerificationCode] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    //   onLogin(username, password, verificationCode);
  };

  return (
    <div className="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-50 p-8 bg-white shadow-md rounded-lg">
      <span
        className="absolute top-4 right-4 cursor-pointer text-2xl text-blue-500"
        onClick={onClose}
      >
        ×
      </span>
      <div className="modal-content">
        <h2 className="text-lg font-semibold mb-4">登录</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="用户名"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="w-full mb-2 px-3 py-2 border rounded"
          />
          <input
            type="password"
            placeholder="密码"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full mb-2 px-3 py-2 border rounded"
          />
          <input
            type="text"
            placeholder="验证码"
            value={verificationCode}
            onChange={(e) => setVerificationCode(e.target.value)}
            className="w-full mb-2 px-3 py-2 border rounded"
          />
          <button
            type="submit"
            className="w-full bg-blue-500 text-white py-2 rounded"
          >
            登录
          </button>
          <div>
            <a href="#" className="text-blue-500">
              忘记密码
            </a>
            <span>
              {" "}
              没有账号？{" "}
              <a href="#" className="text-blue-500">
                注册
              </a>
            </span>
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginForm;
