import React, { useRef } from "react";

const Home = () => {
  return (
    <div>
      <h2 className=" text-3xl">Rice Area Over Time in Gwalior</h2>
      <img src="http://localhost:5000/plot" alt="Plot" />
    </div>
  );
};

export default Home;