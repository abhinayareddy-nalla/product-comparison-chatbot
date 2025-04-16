import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');
  const [userId] = useState('user123'); // You can make this dynamic if needed

  const sendMessage = async () => {
    try {
      const res = await axios.post('http://127.0.0.1:8000/chat', {
        user_id: userId,
        message: message,
      });

      setResponse(res.data.response || res.data.received_message); // depending on what you return
    } catch (error) {
      setResponse('Error contacting backend: ' + error.message);
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h2>Product Comparison Chatbot</h2>
      <textarea
        rows="4"
        cols="50"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask me about products..."
      />
      <br />
      <button onClick={sendMessage}>Send</button>
      <div style={{ marginTop: '20px', whiteSpace: 'pre-wrap' }}>
        <strong>Response:</strong>
        <p>{response}</p>
      </div>
    </div>
  );
}

export default App;
