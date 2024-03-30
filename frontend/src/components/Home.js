import React from 'react';
import orange from "../images/hero-gif.gif"
function Home() {
  return (
    <div className="relative">

      <div className='flex-col'>
        <div className='flex'>
          <div className='mt-10 w-2/3 flex-col text-left'>
            <h2 className='text-5xl text-orange-500 text-left mr-20 mt-12 ml-10 gilroy-semibold'>
            Revolutionize Agriculture <br/>Innovate with <br/>   Agro-Help Solutions
            </h2>
            <div className='mt-5 ml-10 gilroy-medium text-black text-xl mr-60'>From Roots to Results</div>

            <button className="transition delay-150 hover:text-white mt-5 ml-10 hover:bg-black hover:-translate-y-1 hover:scale-110 duration-100 rounded-md p-2 bg-black text-white">
              <a href="http:\\localhost:8501">Data Analysis</a>
            </button>


          </div>
          <img className='mr-24 w-[450px]' src={orange}></img>
        </div>

      </div>

    </div>
  );
}

export default Home;