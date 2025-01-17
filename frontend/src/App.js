import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [userId, setUserId] = useState('');
  const [logs, setLogs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchLogs = async () => {
    if (!userId) return;
    
    setLoading(true);
    setError(null);
    
    try {
      const response = await axios.get(`http://localhost:5000/logs/${userId}`);
      setLogs(response.data);
    } catch (err) {
      setError('Failed to fetch logs');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Activity Log Viewer</h1>
      <div className="search-container">
        <input
          type="text"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          placeholder="Enter User ID"
        />
        <button onClick={fetchLogs}>Fetch Logs</button>
      </div>

      {loading && <p>Loading...</p>}
      {error && <p className="error">{error}</p>}
      
      <div className="logs-container">
        {logs.map((log) => (
          <div key={log.id} className="log-item">
            <h3>Activity: {log.activity}</h3>
            <p>Timestamp: {new Date(log.timestamp).toLocaleString()}</p>
            <p>Metadata: {JSON.stringify(log.metadata)}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
