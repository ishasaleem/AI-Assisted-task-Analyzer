import React, { useState } from "react";
import axios from "axios";
import "./App.css"; // import CSS

function App() {
  const [brief, setBrief] = useState("");
  const [tasks, setTasks] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeBrief = async () => {
    if (!brief) return;

    setLoading(true);
    try {
      const response = await axios.post("http://127.0.0.1:5001/analyze", {
        brief: brief,
      });
      setTasks(response.data);
    } catch (error) {
      console.error(error);
      alert("Failed to fetch tasks from backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>AI Agent Task Analyzer</h1>

      <div className="input-section">
        <textarea
          placeholder="Enter your project brief..."
          value={brief}
          onChange={(e) => setBrief(e.target.value)}
        ></textarea>
        <button onClick={analyzeBrief}>
          {loading ? "Analyzing..." : "Analyze Brief"}
        </button>
      </div>

      {tasks && (
        <div className="tasks-container">
          <div className="task-card">
            <h2>Backend Tasks</h2>
            <ul>
              {tasks.backend.map((task, index) => (
                <li key={index}>{task}</li>
              ))}
            </ul>
          </div>

          <div className="task-card">
            <h2>Frontend Tasks</h2>
            <ul>
              {tasks.frontend.map((task, index) => (
                <li key={index}>{task}</li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
