import React from "react";

const Navbar = () => {
  return (
    <div className="flex h-[75px] bg-green-500 ">
      <img src="" alt="logo" className="p-2 mt-3"></img>
      <ul className="flex p-2  ml-[350px] mt-3">
        <li>Home</li>
        <li className="ml-[150px]">Chat-bot</li>
      </ul>
    </div>
  );
};

export default Navbar;
