<<<<<<< HEAD
import React, { useRef } from "react";
import Navbar from "./Navbar";
=======
import React, { useRef, useState } from "react";
import Navbar from "./components/Navbar";
import Filter from "./components/Filter";
>>>>>>> 37249be4b5ebad51f3c2d7d332f22285d5b8467d

const App = () => {
  return (
    <div>
<<<<<<< HEAD
 
      <h2 className=" text-3xl">Rice Area Over Time in Gwalior</h2>
      <input
        ref={ref}
        type="text"
        name="inputField"
        id="inputField"
        className="border border-black mt-[40px] "
      ></input>
      <img src="http://localhost:5000/plot" alt="Plot" />
=======
      <Navbar />
      <Filter />
>>>>>>> 37249be4b5ebad51f3c2d7d332f22285d5b8467d
    </div>
  );
};

export default App;
