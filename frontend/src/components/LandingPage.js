import { SignInButton } from "@clerk/clerk-react";
import React from "react";
import logo from "../images/eco.gif";

const LandingPage = () => {
  return (
    <>
      <div className="flex">
        <img className="rounded-full w-24 ml-8" src={logo}></img>
        <h1 className="gilroy-bold text-3xl mt-12 ml-2">Agro-help</h1>
        <div className="w-66 ml-33 sticky"></div>
      </div>
      <div className="ml-[40%] mt-[5%] flex  shadow-md w-[130px]  items-center    hover:shadow-xl">
        <div className="p-2 m-4 items-center gilroy-bold text-2xl">
          <SignInButton mode="modal" forceRedirectUrl={"/Home"} />
        </div>
      </div>
    </>
  );
};

export default LandingPage;
