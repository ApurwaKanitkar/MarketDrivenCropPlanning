import React, { useRef, useState } from "react";
import Navbar from "./components/Navbar";
import Filter from "./components/Filter";

const App = () => {
  return (
    <div>
      <Navbar />
      <Filter />
    </div>
  );
};

export default App;
