<<<<<<< HEAD
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
=======
import React, { useRef, useState } from "react";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import Vision from "./components/Vision";
import Services from "./components/Services";
import Contact from "./components/Contact"

import {
  BrowserRouter as Router,
} from "react-router-dom";
import { Routes, Route } from 'react-router-dom';

const App = () => {
  return (
    <>
       <div className='h-screen w-screen overflow-x-scroll no-scrollbar'>
        <Router>
          <Navbar />
          <Routes>
            <Route exact path="/web" element={<Home />}></Route>
            <Route exact path="/Vision" element={<Vision />}></Route>
            <Route exact path="/Services" element={<Services />}></Route>
            <Route exact path="/Contact" element={<Contact />}></Route>
          </Routes>
        </Router>
      </div>
    </>
>>>>>>> 5925b8a72cb42d9683564ba7d7e47823ffb13c5b
  );
};

export default App;
