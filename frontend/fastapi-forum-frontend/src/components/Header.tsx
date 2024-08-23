import MenuItem from "./MenuItem";

const Header: React.FC = () => {
  return (
    <div className="bg-gray-800 text-white flex justify-around items-center rounded border-2 border-gray-600">
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

export default Header;
