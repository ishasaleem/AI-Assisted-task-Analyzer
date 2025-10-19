import { useState } from "react";
import axios from "axios";
import TaskList from "../components/TaskList";

export default function Home() {
  const [brief, setBrief] = useState("");
  const [tasks, setTasks] = useState({ backend: [], frontend: [] });
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!brief) return;
    setLoading(true);
    try {
      const res = await axios.post("http://127.0.0.1:5001/analyze", { brief });
      setTasks(res.data);
    } catch (err) {
      alert("Failed to get tasks from backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6">
      <textarea
        value={brief}
        onChange={(e) => setBrief(e.target.value)}
        placeholder="Enter project brief here..."
        className="w-full p-2 mb-4 border rounded"
        rows={4}
      />
      <button
        onClick={handleAnalyze}
        className="bg-purple-500 text-white px-4 py-2 rounded hover:bg-purple-600"
      >
        {loading ? "Analyzing..." : "Analyze Brief"}
      </button>

      <div className="mt-6">
        {tasks.backend.length > 0 && <TaskList title="Backend Tasks" tasks={tasks.backend} />}
        {tasks.frontend.length > 0 && <TaskList title="Frontend Tasks" tasks={tasks.frontend} />}
      </div>
    </div>
  );
}
