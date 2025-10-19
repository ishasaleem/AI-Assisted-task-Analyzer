import json
from agents.coordinator_agent import CoordinatorAgent
from pathlib import Path

def test_coordinator_creates_task_file(tmp_path, monkeypatch):
    # run coordinator with a simple brief and redirect outputs path to tmp
    monkeypatch.chdir(tmp_path)
    c = CoordinatorAgent()
    brief = "Build a simple app with login and tasks"
    c.process_brief(brief)

    out_file = Path("outputs/tasks/task_breakdown.json")
    assert out_file.exists()
    data = json.loads(out_file.read_text())
    assert "frontend" in data and "backend" in data
