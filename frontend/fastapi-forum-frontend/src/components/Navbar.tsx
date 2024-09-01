"use client";
import React, { useEffect, useState } from "react";
import Navbaritem from "./Navbaritems";
import LoginForm from "./LoginForm";
import SignForm from "./SignupForm";
import { Button } from "./ui/button";

const Navbar: React.FC = () => {
  const [showLoginForm, setShowLoginForm] = useState(false);
  const [showSignForm, setShowSignForm] = useState(false);

  const handleLoginClick = () => {
    setShowLoginForm(true);
  };

  const handleCloseLogin = () => {
    setShowLoginForm(false);
  };

  const handleSignClick = () => {
    setShowSignForm(true);
  };

  const handleCloseSign = () => {
    setShowSignForm(false);
  };

  return (
    <div
      style={{ position: "fixed", top: 0, left: 0, width: "100%", zIndex: 999 }}
      className="bg-gray-800 text-white flex pt-2 pb-1 justify-between rounded boder-2 border-gray-600 gap-4"
    >
      <Navbaritem title="Fastapi-fourm" />
      <Navbaritem title="Message" />
      <Navbaritem title="talk" />
      <Navbaritem title="Search" />
      <Navbaritem title="Search" />
      <Button onClick={handleLoginClick}>Login</Button>
      <Button onClick={handleSignClick}>Sign Up</Button>
      {showLoginForm && <LoginForm onClose={handleCloseLogin} />}
      {showSignForm && <SignForm onClose={handleCloseSign} />}
    </div>
  );
};

export default Navbar;
