import React, { useState } from 'react';
import chatbotlogo from "../images/chatbot-logo.svg"

const ChatBot = () => {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');

  const handleAsk = async () => {
    try {
      const res = await fetch('http://localhost:5000/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question }),
      });
      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      
      <h2 className='flex justify-center text-bold text-2xl'>
        <img className="h-10 w-10" src={chatbotlogo}></img>
        Agri-Bot
      </h2>
      <div className='text-center'>
      <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask a question"
            class="w-60 h-10 bg-transparent text-black font-serif font-lg font-bold outline outline-0 focus:outline-0 disabled:bg-blue-gray-50 transition-all placeholder-shown:border-blue-gray-200 border focus:border-2 border-t-transparent text-sm px-3 py-2.5 rounded-[7px] focus:border-gray-900"
             />
        <button onClick={handleAsk} class="w-14 h-10 m-10 rounded-md transition delay-150 bg-black text-white hover:-translate-y-0.2 hover:scale-110 hover:bg-green-500 duration-300">Ask</button>
      </div>
      <div className="response-container">
        <p className="ml-20 mr-20 text-justify">{response}</p>
      </div>
    </div>
  );
};

export default ChatBot;