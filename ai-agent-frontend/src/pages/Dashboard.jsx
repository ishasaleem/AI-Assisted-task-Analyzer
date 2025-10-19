import React, { useState } from "react";
import axios from "axios";
import TaskCard from "../components/TaskCard";

const Dashboard = () => {
  const [brief, setBrief] = useState("");
  const [tasks, setTasks] = useState({ frontend: [], backend: [] });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:5001/analyze", { brief });
      setTasks(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Dashboard</h2>
      <form onSubmit={handleSubmit} className="mb-6">
        <input
          type="text"
          placeholder="Enter project brief..."
          value={brief}
          onChange={(e) => setBrief(e.target.value)}
          className="w-full border px-3 py-2 rounded mb-2"
        />
        <button
          type="submit"
          className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600"
        >
          Generate Tasks
        </button>
      </form>

      <TaskCard type="Frontend" tasks={tasks.frontend} />
      <TaskCard type="Backend" tasks={tasks.backend} />
    </div>
  );
};

export default Dashboard;
