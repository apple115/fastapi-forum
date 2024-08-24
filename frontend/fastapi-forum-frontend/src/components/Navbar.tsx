"use client";
import React, { useEffect, useState } from "react";
import Navbaritem from "./Navbaritems";
import LoginForm from "./LoginForm";

const Navbar: React.FC = () => {
  const [showLoginForm, setShowLoginForm] = useState(false);

  const handleLoginClick = () => {
    setShowLoginForm(true);
  };

  const handleCloseLogin = () => {
    setShowLoginForm(false);
  };

  return (
    <div
      style={{ position: "fixed", top: 0, left: 0, width: "100%", zIndex: 999 }}
      className="bg-gray-800 text-white flex pt-2 pb-1 justify-between rounded border-2 border-gray-600 gap-4"
    >
      <Navbaritem title="Fastapi-fourm" />
      <Navbaritem title="Message" />
      <Navbaritem title="talk" />
      <Navbaritem title="Search" />
      <button onClick={handleLoginClick}>Login</button>
      {showLoginForm && <LoginForm onClose={handleCloseLogin} />}
    </div>
  );
};

export default Navbar;
