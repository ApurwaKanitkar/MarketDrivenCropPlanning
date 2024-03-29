import React from 'react';
import { Link } from 'react-router-dom';

function App() {
  return (
    <div>
      <h1>Recommendations</h1>
      <Link to="http://localhost:8501">Get Crop Combinations</Link>
    </div>
  );
}

export default App;
