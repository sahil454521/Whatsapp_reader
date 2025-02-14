import React, { useState } from 'react';

function App() {
  const [command, setCommand] = useState('');

  const handleListen = async () => {
    const response = await fetch('/listen', { method: 'POST' });
    const data = await response.json();
    setCommand(data.command);
  };

  return (
    <div>
      <h1>AI WhatsApp Reader</h1>
      <button onClick={handleListen}>Listen</button>
      <p>Command: {command}</p>
    </div>
  );
}

export default App;