"use client";

import Link from "next/link";

interface NavbaritemsProps {
  title:string;
  params?:string;
}


const Navbaritem:React.FC<NavbaritemsProps>=({title,params})=>{
  return (
    <div className="p-2 hover:bg-gray-200 rounded transition-colors duration-200">
      <Link href={`/?`} className="text-white-800 font-semibold">
        {title}
      </Link>
    </div>
  )
}

export default Navbaritem
