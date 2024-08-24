import Link from "next/link";
import React from "react";

interface MenuItemProps {
  title: string;
  address: string;
  Icon?: React.ComponentType
}

const MenuItem: React.FC<MenuItemProps> = ({ title, address, Icon }) => {
  return (
    <Link href={address} className="hover:text-amber-500">
      <p className="text-xs uppercase hidden sm:inline text-xs">{title}</p>
    </Link>
  );
};

export default MenuItem
