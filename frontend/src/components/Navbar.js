import React from "react";
import {
  Link,
} from "react-router-dom";
import logo from "../images/logo.svg"

function Navbar() {

  return (
    <div>
      <div className="bg-green-500 flex sticky">
        <img className="h-10 w-10 m-5" src={logo} />
        <nav className="absolute top-0 right-0 m-5 gap-5 text-white">
          <Link to="/Web" className="m-5 transition duration-0.3 hover:text-yellow-700">
            Home
          </Link>
          <Link to="/Services" className="m-5 transition duration-0.3 hover:text-yellow-700">
            Services
          </Link>
          <Link to="/Testimonials" className="m-5 transition duration-0.3 hover:text-yellow-700">
            Testimonials
          </Link>
          <Link to="/Vision" className="m-5 transition duration-0.3 hover:text-yellow-700">
            Our Vision
          </Link>
          <Link to="/Contact" className="m-5 transition duration-0.3 hover:text-yellow-700">
            Contact Us
          </Link>
        </nav>
      </div>
    </div>
  );
}

export default Navbar;
