import React, { useRef, useState } from "react";
import Navbar from "./components/Navbar";
import Filter from "./components/Filter";

const App = () => {
  return (
    <div>
      <Navbar />
      <Filter />
      <img src="http://localhost:5000/plot" alt="plot"></img>
    </div>
  );
};

export default App;
