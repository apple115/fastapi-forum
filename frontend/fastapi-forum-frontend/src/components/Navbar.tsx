import Navbaritem from "./Navbaritems";

const Navbar:React.FC=()=>{
return (
  <div className="bg-gray-800 text-white flex pt-2 pb-1 justify-between rounded border-2 border-gray-600 gap-4">
    <Navbaritem title="Fastapi-fourm" />
    <Navbaritem title="Message" />
    <Navbaritem title="talk" />
    <Navbaritem title="Search" />
    <Navbaritem title="Login" />
  </div>
  )
}

export default Navbar
