import React, { useRef } from "react";
import Navbar from "./components/Navbar";
import Filter from "./components/Filter";

const App = () => {
  return (
    <div>
      <h2 className=" text-3xl">Rice Area Over Time in Gwalior</h2>
      <input
        type="text"
        name="inputField"
        id="inputField"
        className="border border-black mt-[40px] "
      ></input>
      <img src="http://localhost:5000/plot" alt="Plot" />
      <Navbar />
      <Filter />
    </div>
  );
};

export default App;
