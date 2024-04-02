import React, { useRef, useState } from "react";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import Vision from "./components/Vision";
import Services from "./components/Services";
import Contact from "./components/Contact";
import { BrowserRouter as Router } from "react-router-dom";
import { Routes, Route } from "react-router-dom";
import Dashboard from "./components/Dashboard";

const App = () => {
  return (
    <>
      <div className="h-screen w-screen overflow-x-scroll overflow-y-scroll no-scrollbar">
        <Router>
          <Navbar />
          <Routes>
            <Route exact path="/" element={<Home />}></Route>
            <Route exact path="/Vision" element={<Vision />}></Route>
            <Route exact path="/Services" element={<Services />}></Route>
            <Route exact path="/Contact" element={<Contact />}></Route>
            <Route exact path="/Dashboard" element={<Dashboard />}></Route>
          </Routes>
        </Router>
      </div>
    </>
  );
};

export default App;
