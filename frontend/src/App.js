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

  );
};

export default App;
