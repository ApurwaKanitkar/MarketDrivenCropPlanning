import React from "react";
import { Link } from "react-router-dom";
import logo from "../images/eco.gif";

function Navbar() {
  return (
    <div className="flex">
      <img className="rounded-full w-24 ml-8" src={logo}></img>
      <h1 className="gilroy-bold text-3xl mt-12 ml-2">Agro-help</h1>
      <div className="w-66 ml-33 sticky">
        <nav className="text-center ml-80 mt-10 gap-15 text-black">
          <Link to="/" className=" m-5 ">
            <button className="gilroy-semibold text-lg hover:border-b-4 hover:border-yellow-500 duration-200 hover:text-black">
              Home
            </button>
          </Link>
          <Link to="/Services" className=" m-5">
            <button className="gilroy-semibold text-lg hover:border-b-4 hover:border-yellow-500 duration-200 hover:text-black">
              Services
            </button>
          </Link>
          <Link to="/Vision" className=" m-5 ">
            <button className="gilroy-semibold text-lg hover:border-b-4 hover:border-yellow-500 duration-200 hover:text-black">
              Vision
            </button>
          </Link>
          <Link to="/Contact" className=" m-5 ">
            <button className="gilroy-semibold text-lg hover:border-b-4 hover:border-yellow-500 duration-200 hover:text-black">
              Contact Us
            </button>
          </Link>
          <Link to="/Dashboard" className=" m-5 ">
            <button className="gilroy-semibold text-lg hover:border-b-4 hover:border-yellow-500 duration-200 hover:text-black">
              Dashboard
            </button>
          </Link>
        </nav>
      </div>
    </div>
  );
}

export default Navbar;
