import React from "react";
import Home from "./components/Home";
import Vision from "./components/Vision";
import Services from "./components/Services";
import Contact from "./components/Contact";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import { Route, createRoutesFromElements } from "react-router-dom";
import Dashboard from "./components/Dashboard";
import { RedirectToSignIn, SignedIn, SignedOut } from "@clerk/clerk-react";
import UserProfilePage from "./components/UserProfilePage";
import SignInPage from "./components/LandingPage";
import LandingPage from "./components/LandingPage";

const router = createBrowserRouter(
  createRoutesFromElements(
    <>
      <Route index element={<LandingPage />} />
      <Route
        path="/home"
        element={
          <>
            <SignedIn>
              <Home />
            </SignedIn>

            <SignedOut>
              <RedirectToSignIn />
            </SignedOut>
          </>
        }
      />
      <Route path="/Vision" element={<Vision />} />
      <Route path="/Services" element={<Services />} />
      <Route path="/Contact" element={<Contact />} />
      <Route path="/Dashboard" element={<Dashboard />} />
      <Route path="/UserProfilePage" element={<UserProfilePage />} />
    </>
  )
);
const App = () => {
  return (
    <>
      <RouterProvider router={router} />
    </>
  );
};

export default App;
