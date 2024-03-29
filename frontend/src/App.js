import React, { useRef } from "react";

const App = () => {
  const ref = useRef(null);
  console.log(ref);
  return (
    <div>
      <h2 className=" text-3xl">Rice Area Over Time in Gwalior</h2>
      <input
        ref={ref}
        type="text"
        name="inputField"
        id="inputField"
        className="border border-black mt-[40px] "
      ></input>
      <img src="http://localhost:5000/plot" alt="Plot" />
    </div>
  );
};

export default App;
