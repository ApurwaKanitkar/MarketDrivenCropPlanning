import React, { useState } from "react";

const Filter = () => {
  const [data, setData] = useState();
  console.log(data);
  return (
    <div className="mt-[50px]">
      <div className="flex ">
        <p className="p-2 mx-8">Area</p>
        <input
          type="text"
          placeholder="Enter the location "
          className=" p-2 border border-black"
          onChange={(e) => {
            setData(e.target.value);
          }}
        ></input>
      </div>
    </div>
  );
};

export default Filter;
