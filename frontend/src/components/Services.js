import React, { useState } from 'react';

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
    <div className="chatbot-container">
      <h2>ChatBot</h2>
      <div className="input-container">
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask a question"
          className="input-field"
        />
        <button onClick={handleAsk} className="ask-button">
          Ask
        </button>
      </div>
      <div className="response-container">
        <p className="response-text">{response}</p>
      </div>
    </div>
  );
};

export default ChatBot;
