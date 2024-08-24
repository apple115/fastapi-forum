import MenuItem from "./MenuItem";

const Header: React.FC = () => {
  return (
    <div style={{ marginTop: '48px' }} className="bg-gray-800 text-white pt-1 pd-1 flex justify-around items-center shadow-md">
      <div className="flex gap-2">
        <MenuItem title="Home" address="/" />
        <MenuItem title="About" address="/about" />
      </div>
      <div className="flex gap-2 ">
        <span className=" bg-blue-600 rounded ">fast-api</span>
        <span className=" text-white font-bold rounded">forum</span>
      </div>
    </div>
  );
};

export default Header;
