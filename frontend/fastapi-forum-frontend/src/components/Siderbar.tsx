import Link from "next/link";
import React from "react";

interface SidebarProps {}

const Sidebar: React.FC<SidebarProps> = () => {
  return (
    <div className="bg-gray-800 text-white p-2 w-48 h-screen flex flex-col justify-between">
      <h2 className="text-xl font-bold mb-4">Forum Menu</h2>
      <ul>
        <li className="mb-2">
          <Link href="/">Home</Link>
        </li>
        <li className="mb-2">
          <Link href="/topics">Topics</Link>
        </li>
        <li className="mb-2">
          <Link href="/users/profile">User Profile</Link>
        </li>
        {/* 可以添加更多的链接 */}
      </ul>
      <div className="text-sm text-gray-400 mt-4">Footer content here...</div>
    </div>
  );
};

export default Sidebar;
