import React from "react";
import Navbaritem from "./Navbaritems";
import MenuItem from "./MenuItem";

const RootLayout: React.FC = () => {
  return (
    <div>
      <Header />
      <div
        style={{
          position: "fixed",
          top: 0,
          left: 0,
          width: "100%",
          zIndex: 999,
        }}
        className="bg-gray-800 text-white p-4 justify-center rounded border-2 border-gray-600 gap-8"
      >
        <Navbaritem title="Fastapi-forum" />
        <Navbaritem title="Message" />
        <Navbaritem title="talk" />
        <Navbaritem title="Search" />
        <Navbaritem title="Login" />
      </div>
    </div>
  );
};

const Header: React.FC = () => {
  return (
    <div className="bg-gray-800 text-white p-4 flex justify-around items-center rounded border-2 border-gray-600">
      <div className="flex gap-6 rounded border-2 border-gray-600">
        <MenuItem title="Home" address="/" />
        <MenuItem title="About" address="/about" />
      </div>
      <div className="flex gap-6 rounded border-2 border-gray-600">
        <span className="text-2xl bg-blue-600 rounded">fast-api</span>
        <span className="text-2xl text-white">forum</span>
      </div>
    </div>
  );
};

export default RootLayout;
